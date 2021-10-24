from oauthlib.oauth1 import (
    RequestTokenEndpoint, RequestValidator
)
from oauthlib.common import Request
from etsy_py.api import EtsyAPI


from .inventory import Inventory


class Api(Inventory):
    api = None
    shop = None

    def __init__(self, api_key):
        self.api = EtsyAPI(api_key=api_key)
        self.shop = Shop(self.api)

    def select_shop(self, shop_name):
        self.shop.set_shop(shop_name)
        self.load_shop_listings()

    def load_shop_listings(self):
        self.shop.set_listings()

    def create_request_token(self, api_key, api_secret):
        request_url = f"/oauth/request_token?scope=listings_w"
        validator = RequestValidator()
        endpoint = RequestTokenEndpoint(validator)
        r = Request(request_url)

        token = endpoint.create_request_token(r, credentials={
            'oauth_consumer_key': api_key,
            'oauth_consumer_secret': api_secret
        })
        print(token['login_url'])


class Shop:
    api = None
    id = None
    name = None
    listings = {'active': None, 'expired': None}

    def __init__(self, api):
        self.api = api

    def set_shop(self, shop_name):
        self.name = shop_name
        self.id = self.get_id_using_name()

    def set_listings(self):
        self.listings['active'] = self.get_active_listings()
        # self.listings['expired'].append(self.get_expired_listings())

    def get_id_using_name(self, shop_name=None):
        if self.name is None:
            self.name = shop_name if \
                shop_name is not None else \
                Exception("No shop name specified")

        request_url = f"/shops/{self.name}"

        r = self.api.get(request_url)
        first_result = r.json()['results'][0]

        return first_result['shop_id']

    def get_active_listings(self):
        results = []
        has_next = True
        page_index = 1
        limit = 100

        while has_next:
            request_url = f"/shops/{self.id}/listings/active?limit={limit}&page={page_index}"
            r = self.api.get(request_url)
            page_results = r.json()['results']

            if len(page_results) > 0:
                results.extend(page_results)
                page_index += 1

            else:
                has_next = False

        return results

    def get_expired_listings(self):
        request_url = f"/shops/{self.id}/listings/expired"

        r = self.api.get(request_url)
        print(r.content)
        results = r.json()['results']

        return results

    def create_listing(self, ):
        """
        Required Fields:
            * quantity - int
            * title - string
            * description - text
            * price - float
            * taxonomy_id - int
            * who_made - enum(i_did, collective, someone_else)
            * is_supply - boolean
            * when_made - enum(2020_2021, 2010_2019, ...)

        :param api:
        :return:
        """
        request_url = f"/listings"
        example_item = {
            'quantity': 3,
            'title': 'test_item',
            'description': 'testestest',
            'price': 1.02,
            'taxonomy_id': 6451,
            'who_made': 'someone_else',
            'is_supply': True,
            'when_made': '2010_2019',
        }

        r = self.api.post(request_url, data=example_item)
        print(r.content)
