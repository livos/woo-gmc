from functools import cmp_to_key
from nturl2path import url2pathname
from woocommerce import API


class WooApi:

    def __init__(self, url, c_key, c_secret, timeout):
        self._url = url
        self._c_key = c_key
        self._c_secret = c_secret
        self._timeout = timeout
        self._connection = self._connect_api()

    @property
    def url(self):
        return self._url

    @property
    def c_key(self):
        return self._c_key

    @property
    def c_secret(self):
        return self._c_secret

    @property
    def timeout(self):
        return self._timeout

    @property
    def connection(self):
        return self._connection

    def _connect_api(self):
        wcapi = API(
            url=self._url,
            consumer_key=self._c_key,
            consumer_secret=self._c_secret,
            timeout=self._timeout
        )
        return wcapi
