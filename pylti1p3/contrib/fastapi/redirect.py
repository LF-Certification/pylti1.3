from fastapi.responses import HTMLResponse, RedirectResponse

from pylti1p3.redirect import Redirect


class FastAPIRedirect(Redirect):
    _location = None
    _cookie_service = None

    def __init__(self, location, cookie_service=None):
        super(FastAPIRedirect, self).__init__()
        self._location = location
        self._cookie_service = cookie_service

    def do_redirect(self):
        return self._process_response(RedirectResponse(self._location))

    def do_js_redirect(self):
        return self._process_response(
            HTMLResponse(
                '<script type="text/javascript">window.location="{}";'
                "</script>".format(self._location)
            )
        )

    def set_redirect_url(self, location):
        self._location = location

    def get_redirect_url(self):
        return self._location

    def _process_response(self, response):
        if self._cookie_service:
            self._cookie_service.update_response(response)
        return response
