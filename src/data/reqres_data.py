from dataclasses import dataclass


@dataclass
class UserReqres:
    name: str
    job: str
    updated_job: list
    email: str


user_reqres = UserReqres(
    name='maks',
    job='qa',
    updated_job=['qa', 'sdet'],
    email='maxim.cudaew@gmail.com'
)
