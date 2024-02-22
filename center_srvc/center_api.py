import allure

from requests import Response
from api_client.api_client import ApiClient


class CenterAPI(ApiClient):
    def __init__(self):
        super().__init__(url=SOME_URL, token=SOME_TOKEN)

    @allure.step
    def get_health(self) -> Response:
        path = "/..."
        return self._get(path=path)
        pass

    @allure.step
    def get_full_info(self, x_id: str) -> Response:
        path = f"/.../{x_id}/"
        return self._get(path=path)

    @allure.step
    def get_objs(self, x_id: str) -> Response:
        path = f"/..../?x_id={x_id}"
        return self._get(path=path)

    @allure.step
    def climate_off(self, x_id: str) -> Response:
        path = f"..../{x_id}/..."
        return self._post(path=path)

    @allure.step
    def climate_on(self, x_id: str, value: int) -> Response:
        path = f"/.../{x_id}/..."
        payload = {"level": value}
        return self._post(path=path, json=payload)

    @allure.step
    def door_close(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def door_open(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def external_sounds(self, x_id: str, target: int) -> Response:
        path = f"/.../{x_id}/.."
        payload = {"volume": target}
        return self._post(path=path, json=payload)

    @allure.step
    def internal_sounds(self, x_id: str, target: int) -> Response:
        path = f"/.../{x_id}/.."
        payload = {"volume": target}
        return self._post(path=path, json=payload)

    @allure.step
    def car_go(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def lights_off(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def lights_on(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def car_stop(self, x_id: str) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)

    @allure.step
    def get_orders(self) -> Response:
        path = "/..."
        return self._get(path=path)

    @allure.step
    def get_active_orders(self) -> Response:
        path = "/...."
        return self._get(path=path)

    @allure.step
    def create_new_order(self, x_id: int, y_id: int, is_anonymous: bool) -> Response:
        path = "/..."
        payload = {
            "x_id": x_id,
            "y_id": y_id,
            "is_anonymous": is_anonymous
        }
        return self._post(path=path, json=payload)

    @allure.step
    def order_complete(self, x_id: int) -> Response:
        path = f"/.../{x_id}/.."
        return self._post(path=path)
