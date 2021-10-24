from inventories import InventoryCsvCreator, InventoryEtsyApiCreator
from inventories._api_etsy_config import get_creds

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
        file='data/rainpos_inventory.csv',
        productID='Manufacturer Product Id,sku',
        productTitle='Product Title',
        productQuantity='Edit Inventory'
    )


def create_etsy_test(creator):
    creds = get_creds()
    return creator.create_inventory(
        shop_name='SarahMaeFabrics',
        etsy_key=creds['api_key'],
        etsy_secret=creds['api_secret']
    )


def main():
    """
    csv_test = create_csv_test(InventoryCsvCreator())

    print(csv_test.get_config('productTitle'))
    csv_test.set_inventory()
    print(csv_test.get_inventory())
    """

    etsy_test = create_etsy_test(InventoryEtsyApiCreator())
    print(etsy_test.config['shop_id'])


if __name__ == "__main__":
    main()
