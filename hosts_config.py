from dataclasses import dataclass
from os import getenv


@dataclass
class Hosts:
    def __init__(self, env: str) -> None:
        self.reqres = getenv(f'{env.upper()}_REQRES')
