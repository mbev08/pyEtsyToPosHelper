from . import Report
from re import match


class StockComparisonReport(Report):

    def set_columns(self):
        self.columns = ['ATTENTION FLAG', 'Product', 'SKU', 'Etsy Quantity', 'RainPOS Quantity', 'Difference']

    def get_difference(self, rain_qty, etsy_qty):
        """
        Calculate the difference between rainPOS and Etsy inventory
        Returns difference(int) and which entity is contains the lesser value

        :param rain_qty:
        :param etsy_qty:
        :return:
        """
        def decide_lesser_inventory_entity():
            if rain_qty == etsy_qty:
                return None
            elif rain_qty < etsy_qty:
                return 'Rain'
            elif etsy_qty < rain_qty:
                return 'Etsy'

        difference = round(rain_qty - etsy_qty, 2)
        lesser_inventory_entity = decide_lesser_inventory_entity()

        return difference, lesser_inventory_entity

    def create_formatted_line(self, data):
        def item_is_bolt():
            indicator = r".*by the 1\/2 Yard"

            if match(indicator, data['etsy']['name']):
                return True
            else:
                return False

        def needs_attention():
            threshold = 2 if item_is_bolt() else 1

            if lesser_qty_entity == 'Rain':
                return True
            elif qty_difference >= threshold or qty_difference <= -threshold:
                return True
            else:
                return False

        qty_difference, lesser_qty_entity = self.get_difference(data['rain']['quantity'], data['etsy']['quantity'])
        line_data = [
            'ATTENTION' if needs_attention() else '',
            data['etsy']['name'],
            data['rain']['sku'],
            data['etsy']['quantity'],
            data['rain']['quantity'],
            qty_difference
        ]
        line = {}
        for column, cell_value in zip(self.columns, line_data):
            print(f"{column}+{cell_value}")
            line[column] = cell_value

        return line

    def create(self):
        self.set_columns()
        self.initiate_dataframe()

        print(self.raw_data)
        # print(item['rain']['sku'] + "  " + item['etsy']['name'])
        # print(f"E:{item['etsy']['quantity']} == R:{item['rain']['quantity']}")
        for item in self.raw_data:
            line = self.create_formatted_line(item)
            self.add_formatted_row(line)

        self.write_results()


