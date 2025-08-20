import pytest
import allure
from methods.order_methods import OrderMethods


class TestGetOrders:

    @allure.title('Проверка получения списка всех заказов')
    def test_get_order_list_success(self):
        with allure.step('Отправить GET-запрос, чтобы получить список заказов'):
            response = OrderMethods.get_orders()

        with allure.step('Проверить, что статус-код равен 200'):
            assert response.status_code == 200

        with allure.step('Проверить наличие orders в ответе'):
            assert 'orders' in response.json()

        with allure.step('Проверить, что orders это список'):
            assert isinstance(response.json()['orders'], list)
