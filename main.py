from etsy import EtsyReader
from rainpos import RainPosReader
from InventoryCompare import CompareStock

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


def main():
    etsy = set_etsy()
    rain = set_rain()

    cs = CompareStock(etsy, rain)
    cs.compare_stock()



if __name__ == "__main__":
    main()
