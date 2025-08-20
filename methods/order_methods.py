import requests
import allure
from data import Urls


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(Urls.CREATE_ORDER_URL, json=body)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders():
        return requests.get(Urls.GET_ORDERS_URL)
