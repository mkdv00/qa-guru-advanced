from dataclasses import dataclass
from requests import Response
from hosts_config import Hosts
from src.utils.base_session import BaseSession


@dataclass
class UserReqres:
    name: str
    job: str
    updated_job: list
    email: str


class ReqresWithEnv:
    def __init__(self, env: str) -> None:
        self.reqres = BaseSession(base_url=Hosts(env).reqres)
        self._authorization_cookie = None

    def login(self, email: str, password: str) -> Response:
        return self.reqres.post(
            url='/login',
            params={'Email': email, 'Password': password},
            headers={'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            allow_redirects=False
        )

    @property
    def authorization_cookie(self):
        return self._authorization_cookie

    @authorization_cookie.setter
    def authorization_cookie(self, response):
        self._authorization_cookie = {"NOPCOMMERCE.AUTH": response.cookies.get("NOPCOMMERCE.AUTH")}


user_reqres = UserReqres(
    name='maks',
    job='qa',
    updated_job=['qa', 'sdet'],
    email='maxim.cudaew@gmail.com'
)
