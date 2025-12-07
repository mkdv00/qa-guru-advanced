import os
import pytest

from typing import Any
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser) -> None:
    parser.addoption('--env', action='store', default='test')


@pytest.fixture(scope='session')
def env(request) -> Any:
    return request.config.getoption('--env')
