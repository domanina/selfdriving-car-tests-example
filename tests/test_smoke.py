import time
import allure
import pytest
import json
import jsonschema

from receiver.const import *
from receiver.helper import validate_schema, check_status_code


@allure.suite("Smoke tests")
@allure.sub_suite("Health")
class TestHealth:
    @allure.title("Ping GEO srvc")
    def test_get_healthx(self, geo_api_client):
        respz = geo_api_client.geo_healthz()
        check_status_code(respz, HTTP_OK)
        respx = geo_api_client.geo_healthx()
        check_status_code(respx, HTTP_OK)



@allure.suite("Smoke tests")
@allure.sub_suite("Integration tests FCC-Coach")
class TestReceiver:
    @allure.title("Get car info")
    def test_get_flip_info(self, center_api_client, api_helper):
        with allure.step("Get info request"):
            resp = center_api_client.get_full_info(x_id=ID)
            check_status_code(resp, HTTP_OK)
            assert api_helper.get_car_relevance(ID) < TIMEOUT, "Car info is out of date"
            try:
                decoded = resp.json()
                assert decoded, "Response is empty"
                validate_schema(decoded, "../schemas/sample_schema.json")
                assert decoded["x_id"] == ID, "Unknown 'xid' in response"
            except json.JSONDecodeError as e:
                raise AssertionError(f"Decode response failed: {e}")
            except jsonschema.exceptions.ValidationError as e:
                raise AssertionError(f"Schema validation failed: {e.message}")

    @pytest.mark.parametrize("params", [20, 30], ids=["MAX_CLIMATE", "MIN_CLIMATE"])
    @allure.title("Turn off and on climate")
    def test_climate(self, center_api_client, api_helper, params):
        api_helper.set_default_climate(x_id=ID, default=DEFAULT, timeout=TIMEOUT)
        with allure.step("Turn off climate"):
            resp = center_api_client.climate_off(ID)
            check_status_code(resp, HTTP_CREATED)
        with allure.step("Wait until setting new state"):
            api_helper.waiting_until(ID, ..., ..., TIMEOUT), "Climate has not turned off"
        with allure.step(f"Turn on climate: {params}"):
            resp = center_api_client.climate_on(ID, params)
            check_status_code(resp, HTTP_CREATED)
        with allure.step(f"Wait until setting new stare: {params} "):
            api_helper.waiting_until(x_id=ID,
                                     parameters=[..., ...],
                                     target_values=[..., params],
                                     timeout=TIMEOUT), "Climate has not turned"

    @allure.title("Open and close the door")
    def test_doors(self, center_api_client, api_helper):
        api_helper.set_default_door_state(ID, TIMEOUT)
        with allure.step("Open the doors"):
            resp = center_api_client.door_open(ID)
            check_status_code(resp, HTTP_CREATED)
        with allure.step("Wait until setting new stare"):
            api_helper.waiting_until(x_id=ID,
                                     parameters=...,
                                     target_values=...,
                                     timeout=TIMEOUT), "Door is still closed"
        with allure.step("Close the doors"):
            resp = center_api_client.door_close(ID)
            check_status_code(resp, HTTP_CREATED)
        with allure.step("Wait until setting new stare"):
            api_helper.waiting_until(x_id=ID,
                                     parameters=...,
                                     target_values=...,
                                     timeout=TIMEOUT), "Door is still opened"



@allure.suite("Smoke tests")
@allure.sub_suite("Api tests GEO srvc")
class TestGEO:
    @allure.title("Get maps from GEO by something")
    def test_get_map(self, geo_api_client):
        resp = geo_api_client.get_near_obj(..., ...)
        check_status_code(resp, HTTP_OK)
        try:
            decoded = resp.json()
            with allure.step("Validate response format"):
                assert decoded, "Response is empty"
            with allure.step("Validate json schema"):
                validate_schema(decoded, "../schemas/sample_schema.json")
            with allure.step("Validate response data"):
                assert decoded["items"], "List is empty"
                assert decoded["items"][0]["id"] == ..., "Error..."
        except json.JSONDecodeError as e:
            raise AssertionError(f"Decode response failed: {e}")
        except jsonschema.exceptions.ValidationError as e:
            raise AssertionError(f"Response schema validation failed: {e.message}")
