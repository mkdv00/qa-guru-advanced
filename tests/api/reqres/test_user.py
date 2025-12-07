import pytest
from pytest_voluptuous import S

from src.data.reqres_data import user_reqres
from src.schemas.reqres_schemas import reqres_get_user_schema


class TestUser:
    BASE_ENDPOINT = '/api/users'

    @pytest.mark.parametrize(
        'user_id',
        [2],
        ids=['get-user-by-id']
    )
    def test_get_user_ok(self, user_id, reqres) -> None:
        response = reqres.get(f'{self.BASE_ENDPOINT}/{user_id}')
        response_json = response.json()
        response_data = response_json.get('data')
        expected_status_code = 200

        assert response.status_code == expected_status_code, (f'Wrong status code - {response.status_code}, '
                                                              f'expected - {expected_status_code}')
        assert S(reqres_get_user_schema) == response.json(), f'Wrong response schema'
        assert response_data.get('first_name') == user_reqres.first_name, (
            f'Wrong first name - {response_data.get("first_name")}, expected - {user_reqres.first_name}')
        assert response_data.get('last_name') == user_reqres.last_name, (
            f'Wrong last name - {response_data.get("last_name")}, expected - {user_reqres.last_name}')
        assert response_data.get('email') == user_reqres.email, (
            f'Wrong email - {response_data.get("email")}, expected - {user_reqres.email}')
