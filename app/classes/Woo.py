import os

from ..common.common_helper import load_settings
from ..data.remote.apis.woo.dal import get_all_products
from ..data.remote.apis.woo.Connection import WooApi
from ..classes.WooProduct import WooProduct

settings = load_settings()


class Woo():
    api = None

    def __init__(self):
        self._url = os.getenv('URL')
        self._language = settings["merchant center"]["language"]
        self._country = settings["merchant center"]["country"]

        consumer_key = os.getenv('C_KEY')
        consumer_secret = os.getenv('C_SECRET')
        timeout = settings["woo api"]["timeout"]
        self.api = WooApi(self._url, consumer_key, consumer_secret,
                          timeout).connection

    def all_products(self):
        products = get_all_products(self.api)
        products_arr = []
        for p in products:
            woo_product = WooProduct(p["id"],
                                     p["name"],
                                     p["description"],
                                     p["permalink"],
                                     p["images"],
                                     p["price"],
                                     p["sale_price"])
            products_arr.append(woo_product)
            break
        return products_arr

    @property
    def url(self):
        return self._url

    @property
    def language(self):
        return self._language

    @property
    def country(self):
        return self._country
