def get_all_products(wcapi):
    response = wcapi.get("products", params={"per_page": 100})
    products = response.json()
    return products
