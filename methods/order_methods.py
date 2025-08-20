import requests
import allure
from data import URL


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(URL.CREATE_ORDER_URL, json=body)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders():
        return requests.get(URL.GET_ORDERS_URL)
