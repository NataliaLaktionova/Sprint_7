import requests
import allure
import pytest
from data import Data
from helpers import create_random_login, create_random_password
from url import URLS


class Test_login_courier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_successful_login_courier(self):
        response = requests.post(URLS.URL_LOGIN_COURIER, data=Data.correct_courier_info)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка получения ошибки авторизации курьера при вводе невалидных данных')
    @pytest.mark.parametrize('invalid_data', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_info_with_invalid_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, invalid_data):
        response = requests.post(URLS.URL_LOGIN_COURIER, data=invalid_data)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка получения ошибки авторизации курьера с пустым полем логина/пароля')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': Data.password},
        {'login': Data.login, 'password': ''}
    ])
    def test_courier_login_with_empty_fields(self, empty_fields):
        response = requests.post(URLS.URL_LOGIN_COURIER, data=empty_fields)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}