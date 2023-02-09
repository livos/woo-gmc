1. Download file `content-api-key.json` by creating an API key in Google Merchant Center
2. Rename it to `service-account.json` and place it in `home/shopping-samples/content/` (*This path is defined in /shopping/content/common.py file in the project*)
3. Create an empty `merchant-info.json` file in this same directory and add this code in it:
    ```xml
    {
        "merchantId": your Merchant Center merchant ID,
        "accountSampleUser": "the email address in merchant center > settings > Content API > Authentication (in the user column)"
    }
    ```
4. Download the [Python sample project from Google](https://github.com/googleads/googleads-shopping-samples/tree/main/python)
5. Create a virtual env
6. install the project with `pip install -r requirements.txt`
7. Create a product with ` python -m shopping.content.products.lvs-insert`
8. Check if the product has been created with [Api Explorer](https://developers.google.com/shopping-content/reference/rest/v2.1/products/list?apix=true) or in Merchant Center. Note that the inserted product can appear in Api Explorer and MC after some minuts of delay.

