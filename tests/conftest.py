import pytest

from geo_srvc.geo_api import GeoAPI
from center_srvc.center_api import CenterAPI
from receiver.helper import ApiHelper


@pytest.fixture(scope="session")
def geo_api_client():
    api = GeoAPI()
    yield api
    del api


@pytest.fixture(scope="session")
def center_api_client():
    api = CenterAPI()
    yield api
    del api


@pytest.fixture(scope="session")
def api_helper():
   api = ApiHelper()
   yield api
   del api
