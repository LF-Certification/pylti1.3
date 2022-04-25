from pylti1p3.request import Request


class FastAPIRequest(Request):
    _request = None
    _default_params = None

    @property
    def session(self):
        return self._request.session

    def __init__(self, request, post_only=False, default_params=None):
        self.set_request(request)
        self._default_params = default_params if default_params else {}

    def set_request(self, request):
        self._request = request

    def get_param(self, key):
        return self._request.query_params.get(key, self._default_params.get(key))
 
    def get_cookie(self, key):
        return self._request.cookies.get(key)

    def is_secure(self):
        return self._request.url.scheme == "https"
