from inventories import InventoryCsvCreator, InventoryApiCreator
from InventoryCompare import CompareStock

"""

STORE_NAME = "SarahMaeFabrics"

API_KEY = None
API_SECRET = None


def set_etsy():
    etsy = EtsyReader(API_KEY)
    etsy.select_shop(STORE_NAME)
    return etsy


def set_rain():
    rain = RainPosReader('data/9330-edit-inventory(1).csv')
    rain.set_data()
    return rain
"""


def create_csv_test(creator):
    return creator.create_inventory(
        directory='data',
        productID='Manufacturer Product Id,sku',
        productTitle='Product Title',
        productQuantity='Edit Inventory'
    )


def main():
    csv_test = create_csv_test(InventoryCsvCreator())

    print(csv_test.get_config('productTitle'))
    csv_test.set_inventory()
    print(csv_test.get_inventory())


if __name__ == "__main__":
    main()
