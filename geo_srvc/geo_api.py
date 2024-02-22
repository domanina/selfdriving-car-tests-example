import allure

from requests import Response
from api_client.api_client import ApiClient
from receiver.helper import check_status_code


class GeoAPI(ApiClient):
    def __init__(self):
        super().__init__(url=SOME_URL, token=SOMETOKEN)

    @allure.step
    def geo_healthx(self) -> Response:
        path = "/..."
        return self._get(path=path)

    @allure.step
    def geo_healthz(self) -> Response:
        path = "/..."
        return self._get(path=path)

    @allure.step
    def get_near_obj(self, lats: float, lons: float) -> Response:
        path = f"/...lat={last}&lon={lons}"
        return self._get(path=path)

    @allure.step
    def get_obj_by_id(self, x_id: int) -> Response:
        path = f"/...?x_id={x_id}"
        return self._get(path=path)

    @allure.step
    def get_geo_route(self, x_id: int) -> Response:
        path = f"/...?x_id={x_id}"
        return self._get(path=path)

    @allure.step
    def get_geo_route_by_something(self, x_id: int) -> Response:
        path = f"/../{x_id}"
        return self._get(path=path)
