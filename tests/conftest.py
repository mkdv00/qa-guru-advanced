import pytest
import logging

from typing import Any
from dotenv import load_dotenv
from src.utils.base_session import BaseSession
from src.data.reqres_data import ReqresWithEnv

load_dotenv()


def pytest_addoption(parser) -> None:
    parser.addoption('--env', action='store', default='test')


def pytest_configure() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )


@pytest.fixture(scope='session')
def env(request) -> Any:
    return request.config.getoption('--env')


@pytest.fixture(scope='session')
def reqres(env) -> BaseSession:
    return ReqresWithEnv(env).reqres
