import json


class WooProduct:
    def __init__(self,
                 id,
                 name,
                 description,
                 permalink,
                 images,
                 price,
                 sale_price):
        self._id = id
        self._name = name
        self._description = description
        self._permalink = permalink
        self._images = images
        self._price = price
        self._sale_price = sale_price

    def to_mc_product(self, language, country):
        product = {
            "id": self._id,
            "title": self._name,
            "description": self._description,
            "link": self._permalink,
            "image_link": self._images[0],
            "price": self._price,
            "sale_price": self._sale_price,
            "contentLanguage": language,
            "targetCountry": country,
            "identifier_exists": "true",
            "condition": "new"
        }
        mc_product = json.dumps(product)
        return (mc_product)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def permalink(self):
        return self._permalink

    @property
    def images(self):
        return self._images

    @property
    def price(self):
        return self._price

    @property
    def sale_price(self):
        return self._sale_price
