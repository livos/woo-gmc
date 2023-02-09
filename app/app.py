import os

from app import log
from .data.local.database.helper import sessionScope
from .classes.Woo import Woo

from shopping.content import common

offer_id = 'book#%s' % common.get_unique_id()
product2 = {
    'id': '7321',
    'offerId': '7321',
    'title': 'Porte-ue',
    'description': 'Unforme d’ananas',
    'link': 'https://pxxxr/tique/',
    'imageLink': 'https://pxxxr/que.jpg',
    'condition': 'new',
    'availability': 'in stock',
    'price': {
        'value': '13.90',
        'currency': 'EUR'
    },
    'identifier_exists': 'false',
    'channel': 'online',
    'targetCountry': 'FR',
    'contentLanguage': 'fr'
}

product = {
    'offerId':
    offer_id,
    'title':
    'A Tale of All Cities',
    'description':
    'A classic novel about the French Revolution',
    'link':
    'http://my-book-shop.com/tale-of-two-cities.html',
    'imageLink':
    'http://my-book-shop.com/tale-of-two-cities.jpg',
    'contentLanguage':
    'en',
    'targetCountry':
    'US',
    'channel':
    'online',
    'availability':
    'in stock',
    'condition':
    'new',
    'googleProductCategory':
    'Media > Books',
    'gtin':
    '9780007350896',
    'price': {
        'value': '2.50',
        'currency': 'USD'
    },
    'shipping': [{
        'country': 'US',
        'service': 'Standard shipping',
        'price': {
            'value': '0.99',
            'currency': 'USD'
        }
    }],
    'shippingWeight': {
        'value': '200',
        'unit': 'grams'
    }
}


def run(argv):
    log.debug('app start')

    # Construct the service object to interact with the Content API.
    service, config, _ = common.init(argv, __doc__)

    # Get the merchant ID from merchant-info.json.
    merchant_id = config['merchantId']

    # Create the request with the merchant ID and product object.
    request = service.products().insert(merchantId=merchant_id, body=product2)

    # Execute the request and print the result.
    result = request.execute()
    print('Product with offerId "%s" was created.' % (result['offerId']))

    # with sessionScope(os.getenv('DB_CONNECTION_STRING')) as session:
    #     woo = Woo()
    #     woo_products = woo.all_products()
    #     for w_product in woo_products:
    #         print(f"{w_product.name}\n")
    #         mcprod = w_product.to_mc_product(woo.language, woo.country)
    #         print(f"{mcprod}\n=========================")

    log.debug('app end')
