import pytest
import allure
from methods.order_methods import OrderMethods
from helper import modify_order_data

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с выбором самоката разного цвета')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_different_colors_success(self, color):
        with allure.step('Создать заказ с указанным цветом самоката'):
            order_body = modify_order_data('color', color)

        with allure.step('Отправить POST-запрос на создание заказа'):
            response = OrderMethods.create_order(order_body)

        with allure.step('Проверить, что статус-код равен 201 и в ответе есть track'):
            assert response.status_code == 201
            assert 'track' in response.json()
