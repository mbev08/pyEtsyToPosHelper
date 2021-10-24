from .entity_handler import Etsy, RainPos
from re import match
from reporter import StockComparisonReport


class CompareStock:
    etsy = None
    rainpos = None
    report = StockComparisonReport('data/results/test.CSV')

    def __init__(self, etsy, rainpos):
        self.etsy = Etsy(etsy)
        self.rainpos = RainPos(rainpos)
        self.prep_data()

    def prep_data(self):
        self.etsy.get_data_to_compare()
        self.rainpos.get_data_to_compare()

    def find_matching_from_etsy_list(self):
        def etsy_has_sku():
            if len(etsy_item['sku']) > 0:
                return True

        def find_matching_rain_item():
            for rain_item in self.rainpos.data:
                # print(f"Testing {etsy_item['sku']} vs {rain_item['sku']}")
                # sleep(0.1)
                if rain_item['sku'] in etsy_item['sku']:
                    return True, {'etsy': etsy_item, 'rain': rain_item}
            return False, etsy_item

        matching_items = []
        match_not_found = []
        from time import sleep
        for etsy_item in self.etsy.data:
            if etsy_has_sku():
                has_match, match_result = find_matching_rain_item()
                if has_match:
                    matching_items.append(match_result)
                else:
                    match_not_found.append(match_result)

        return matching_items

    @staticmethod
    def item_is_bolt(item_name):
        indicator = r".*by the 1\/2 Yard"

        if match(indicator, item_name):
            return True
        else:
            return False

    @staticmethod
    def calc_yardage(half_yard_quantity):
        return float(half_yard_quantity / 2)

    def compare_stock(self):
        matching_items = self.find_matching_from_etsy_list()
        report_data = []

        for item in matching_items:
            if self.item_is_bolt(item['etsy']['name']):
                item['etsy']['quantity'] = self.calc_yardage(item['etsy']['quantity'])


            report_data.append(item)

        self.report.set_data(report_data)
        self.report.create()