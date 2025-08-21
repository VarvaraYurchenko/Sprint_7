import pytest
import allure
from methods.order_methods import OrderMethods

@allure.feature('Список заказов')
class TestGetOrders:

    @allure.title('Проверка получения списка всех заказов')
    def test_get_order_list_success(self):
        with allure.step('Отправить GET-запрос, чтобы получить список заказов'):
            response = OrderMethods.get_orders()

        with allure.step('Проверить, что статус-код равен 200'):
            assert response.status_code == 200

        with allure.step('Проверить наличие orders в ответе и что он является списком'):
            assert 'orders' in response.json()
            assert isinstance(response.json()['orders'], list)
