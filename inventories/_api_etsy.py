from re import sub
from oauthlib.oauth1 import (
    RequestTokenEndpoint, RequestValidator
)
from oauthlib.common import Request
from etsy_py.api import EtsyAPI

from .inventory import Inventory
from ._api_etsy_config import get_api_config


SHOP_NAME = 'shop_name'
SHOP_ID = 'shop_id'
ETSY_KEY = 'etsy_key'
ETSY_SECRET = 'etsy_secret'
RESULTS_LIMIT = 'results_limit'
PAGE_INDEX = 'page_index'

GET_SHOP_ID = 'GetShopId'
GET_ACTIVE_LISTINGS = 'GetActiveListings'
GET_EXPIRED_LISTINGS = 'GetExpiredListings'


class ApiEtsy(Inventory):
    config_data_type = {
        SHOP_NAME: str,
        SHOP_ID: str,
        ETSY_KEY: str,
        ETSY_SECRET: str
    }
    api = None
    api_map = get_api_config()

    def validate_config(self, **kwargs) -> bool:
        """
        Required config:
            - Store Name
            - Etsy API Key
            - Etsy API Secret

        :param kwargs:
        """
        try:
            kwargs[SHOP_NAME]
        except KeyError:
            raise Exception("Expecting 'shop_name' values; none were found")

        try:
            kwargs[ETSY_KEY]
        except KeyError:
            raise Exception("Expecting 'etsy_key' values; none were found")

        try:
            kwargs[ETSY_SECRET]
        except KeyError:
            raise Exception("Expecting 'etsy_secret' values; none were found")

    def set_config(self, **kwargs):
        super(ApiEtsy, self).set_config(**kwargs)

        self.api = EtsyAPI(api_key=self.config['etsy_key'])

        self.config[SHOP_ID] = self.__get_shop_id()

    def __format_uri_from_map(self, map_item):
        uri = map_item['URI']

        try:
            uri = self.__format_uri_from_map_populate_vars(uri, map_item['Variables'])
        except KeyError:
            pass

        return uri

    def __format_uri_from_map_populate_vars(self, uri, variables):
        for var in variables:
            print(var)
            mapped_value = self.config[self.api_map['VariablesMapping'][var]]
            print(mapped_value)
            uri = sub(var, mapped_value, uri)

        return uri

    def __send_api_request(self, map_item, only_get_first_result=0):
        request = self.__format_uri_from_map(map_item)
        print(request)
        return self.__get_api_results(self.api.get(request), map_item['Returns'], only_get_first_result)

    @staticmethod
    def __get_api_results(response, return_keyword, only_get_first_result=0):
        print(response)
        if only_get_first_result:
            result = response.json()['results'][0]
        else:
            result = response.json()['results']

        try:
            return result[return_keyword]
        except KeyError:
            return result

    def __get_shop_id(self):
        return self.__send_api_request(self.api_map[GET_SHOP_ID], 1)

    def set_inventory(self): ...





