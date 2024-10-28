import requests
import allure
import pytest
import json
from data import OrderData
from url import URLS

class TestOrderCreate:
    @allure.title('Проверка создания заказа с разными значениями для параметра color')
    @pytest.mark.parametrize('order_data', [
        OrderData.Order_data_1_without_colors, OrderData.Order_data_2_color_black,
        OrderData.Order_data_3_colors_black_and_grey, OrderData.Order_data_4_color_grey
    ])
    def test_order_crete_color_parametrize_success(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URLS.URL_CREATE_ORDERS, data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text