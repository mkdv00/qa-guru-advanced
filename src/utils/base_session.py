import allure
import json
import logging

from json import JSONDecodeError
from curlify import to_curl
from requests import Session, Response
from typing import Callable


def allure_logger(func) -> Callable:
    def wrapper(*args, **kwargs) -> Response:
        method, url = args[1], args[2]

        with allure.step(f'{method} {url}'):
            response: Response = func(*args, **kwargs)

            allure.attach(
                body=to_curl(response.request).encode('utf8'),
                name=f'Request: {response.status_code}'
            )

            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4),
                    name=f'Response: {response.status_code}',
                    attachment_type=allure.attachment_type.JSON,
                    extension='.json'
                )
            except JSONDecodeError:
                allure.attach(
                    body=response.text,
                    name=f'Response: {response.status_code}',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='.txt'
                )

            return response

    return wrapper


def log_request(func) -> Callable:
    def wrapper(*args, **kwargs) -> Response:
        response: Response = func(*args, **kwargs)
        logging.info(f'Request - code: {response.status_code} - {to_curl(response.request)}')
        logging.info(f'Response - {response.json()}')
        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, base_url: str) -> None:
        super(BaseSession, self).__init__()
        self.base_url = base_url

    @allure_logger
    @log_request
    def request(self, method: str, endpoint: str, **kwargs) -> Response:
        response = super().request(
            method=method,
            url=self.base_url + endpoint, **kwargs
        )
        return response
