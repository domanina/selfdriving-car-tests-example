import json
import time
import allure

from datetime import datetime
from requests import Response
from center_srvc.center_api import CenterAPI
from jsonschema import validate
from receiver.const import SOMETHING
from geopy import distance


@allure.step
def validate_schema(data: object, schema_obj: str):
    with open(schema_obj) as f:
        schema = json.load(f)
        validate(instance=data, schema=schema)


@allure.step
def check_status_code(response: Response, status_code: int):
    assert response.status_code == status_code, f"Test failed. HTTP status is : {response.status_code}, {response.text}"


class ApiHelper:
    def  __init__(self):
        self.center_api_client = CenterAPI()

    @allure.step
    def get_car_relevance(self, x_id: str) -> float:
        resp = self.center_api_client.get_full_info(x_id)
        if not resp:
            raise AssertionError("Info is empty")
        decoded = resp.json()
        update_at = datetime.strptime(decoded["update_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        now = datetime.utcnow()
        diff = now - update_at
        return diff.total_seconds()

    @allure.step
    def waiting_until(self, x_id: str, parameters, target_values, timeout: int) -> None:
        waiting = time.time() + timeout
        wrong_parameters = dict()
        while time.time() < waiting:
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()

            if isinstance(parameters, str):
                parameters = [parameters]
                target_values = [target_values]

            assert len(parameters) == len(target_values), "Error..."

            for parameter, arameter_value in zip(parameters, target_values):
                if decoded[parameter] == arameter_value:
                    if parameter in wrong_parameters:
                        wrong_parameters.pop(parameter, None)
                    else:
                        continue
                else:
                    wrong_parameters[parameter] = arameter_value
            time.sleep(1)

        assert not len(wrong_parameters), f"{wrong_parameters=}"

    @allure.step
    def set_default_door_state(self, x_id: str, timeout: int):
        with allure.step("Check door state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded[...] == ...:
                resp = self.center_api_client.door_close(x_id)
                check_status_code(resp, ...)
                self.waiting_until(x_id, ...., ...., timeout)

    @allure.step
    def set_default_lights(self, x_id: str, timeout: int):
        with allure.step("Check lights state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded[...] == ....:
                resp = self.center_api_client.lights_on(x_id)
                check_status_code(resp, ...)
                self.waiting_until(x_id, ..., ..., timeout)

    @allure.step
    def set_default_ext_sounds(self, x_id: str, default: int, timeout: int):
        with allure.step(f"Check ext sounds state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded[...] != ....:
                resp = self.center_api_client.external_sounds(x_id, default)
                check_status_code(resp, ...)
                self.waiting_until(x_id, ..., default, timeout)

    @allure.step
    def set_default_int_sounds(self, x_id: str, default: int, timeout: int):
        with allure.step(f"Check int sounds state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded[....] != default:
                resp = self.center_api_client.internal_sounds(x_id, default)
                check_status_code(resp, ....)
                self.waiting_until(x_id, ...., default, timeout)

    @allure.step
    def set_default_climate(self, x_id: str, default: int, timeout: int):
        with allure.step("Check climate state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded[...] == ... or decoded[...] != default:
                resp = self.center_api_client.climate_on(x_id, default)
                check_status_code(resp, ....)
                self.waiting_until(x_id, [..., ...], [..., default], timeout)

    @allure.step
    def release_car(self, x_id: str, timeout: int) -> None:
        with allure.step("Check car state"):
            resp = self.center_api_client.get_full_info(x_id)
            decoded = resp.json()
            if decoded["..."] and decoded[...] == ....:
                order_id = decoded["..."]["..."]
                resp = self.center_api_client.order_complete(order_id)
                check_status_code(resp, ...)
                self.waiting_until(x_id, ..., ..., timeout)
        with allure.step("Set default states"):
            with allure.step("Сlose doors"):
                self.set_default_door_state(x_id, timeout)
            with allure.step("Set default ext sounds"):
                self.set_default_ext_sounds(x_id, ..., timeout)
            with allure.step("Set default int sounds"):
                self.set_default_int_sounds(x_id, ...., timeout)
            with allure.step("Set default lights"):
                self.set_default_lights(x_id, timeout)
            with allure.step("Set default climate state"):
                self.set_default_climate(x_id, ..., timeout)

    @allure.step
    def is_active_order_exist(self, x_id: str) -> bool:
        with allure.step("Check all active orders"):
            resp = self.center_api_client.get_active_orders()
            check_status_code(resp, HTTP_OK)
            decoded = resp.json()
            x_ids = [khjhjhn["id"] for x in decoded]
            return x_id in x_ids

    @allure.step
    def check_moving_status(self, x_id: str, timeout: int):
        with allure.step("Check ...."):
            self.waiting_until(x_id,
                               [..., ..., ],
                               timeout), " Wrong actuation mode"

    @allure.step
    def is_relevant_distance(self, cur_loc, poi, radius) -> bool:
        d = distance.distance(cur_loc, poi).m
        return d < radius

