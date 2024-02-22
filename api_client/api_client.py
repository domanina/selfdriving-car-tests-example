import requests
from requests import request, Response


class ApiClient:
    def __init__(self, url, token):
        self._url = url
        self._token = token

    @property
    def url(self):
        return self._url

    def _do_request(self, method: str, path: str, **kwargs) -> Response:
        headers = {
            "Accept": "application/json",
            "Authorization": self._token
        }
        url = self.url + path
        try:
            response = request(method=method, url=url, headers=headers, verify=False, **kwargs)
            return response
        except requests.RequestException as e:
            raise AssertionError(f"Request failed. Path: {path}. Error: {e}")

    def _get(self, path, **kwargs):
        return self._do_request("GET", path, **kwargs)

    def _post(self, path, **kwargs):
        return self._do_request("POST", path, **kwargs)

    def _delete(self, path, **kwargs):
        return self._do_request("DELETE", path, **kwargs)



