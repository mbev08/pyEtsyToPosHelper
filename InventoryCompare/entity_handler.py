from abc import abstractmethod
from re import sub, match


class Entity:
    def __init__(self, entity):
        self.entity = entity
        self.data = []

    @abstractmethod
    def get_data_to_compare(self):
        pass


class Etsy(Entity):
    def get_data_to_compare(self):
        """
        Data to establish and return via a Dict

        1.) SKU
        2.) Quantity

        :return:
        """
        for item in self.entity.shop.listings['active']:
            match(r'Precut.*', item['title']) and print(item)
            self.data.append({
                'name': item['title'],
                'sku': item['sku'],
                'quantity': float(item['quantity']),
            })


class RainPos(Entity):
    def get_data_to_compare(self):
        """
        Data to establish and return via a Dict

        1.) ManuID > SKU
        2.) Quantity

        :return:
        """
        def get_sku(val):
            return sub(r"^\=|\"", r"", val)

        for index, item in self.entity.data.iterrows():
            self.data.append({
                'name': item['Product Title'],
                'sku': get_sku(item['Manufacturer Product Id']) if get_sku(item['Manufacturer Product Id']) != '' else get_sku(item['sku']),
                'quantity': item['Edit Inventory'],
            })



