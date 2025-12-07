from dataclasses import dataclass


@dataclass
class UserReqres:
    name: str
    job: str
    updated_job: list
    email: str
