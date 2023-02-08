import os

from app import log
from .data.local.database.helper import sessionScope
from .classes.Woo import Woo


def run():
    log.debug('app start')

    with sessionScope(os.getenv('DB_CONNECTION_STRING')) as session:
        woo = Woo()
        woo_products = woo.all_products()
        for w_product in woo_products:
            print(w_product.name)
            mcprod = w_product.to_mc_product(woo.language, woo.country)
            print(mcprod)
    log.debug('app end')
