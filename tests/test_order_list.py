import requests
import allure
from url import URLS

class Test_get_list_orders:
    @allure.title('Проверка успешного получения списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(URLS.URL_CREATE_ORDERS)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]