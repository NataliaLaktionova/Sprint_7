import requests
import allure
import pytest
from data import Data
from helpers import create_random_login, create_random_password, create_random_firstname
from url import URLS

class Test_create_courier:
    @allure.title('Проверка успешного создания аккаунта курьера')
    def test_create_courier_account_success(self):
        info = {
            'login': create_random_login(),
            'password': Data.password,
            'firstName': Data.firstname
        }
        response = requests.post(URLS.URL_CREATE_COURIER, data=info)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка получения ошибки при дублировании одного логина в создании курьера')
    def test_create_courier_account_login_taken_conflict(self):
        info = {
            'login': Data.login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(URLS.URL_CREATE_COURIER, data=info)
        assert response.status_code == 409 and response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Проверка получения ошибки при создании курьера с пустыми обязательными полями')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()},
    ])
    def test_create_courier_with_empty_required_fields(self, empty_fields):
        response = requests.post(URLS.URL_CREATE_COURIER, data=empty_fields)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}