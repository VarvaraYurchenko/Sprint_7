import requests
import allure
from data import URL


class CourierMethods:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(body):
        return requests.post(URL.CREATE_COURIER_URL, json=body)

    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(login, password):
        return requests.post(URL.LOGIN_COURIER_URL, json={"login": login, "password": password})

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(URL.DELETE_COURIER_URL + f"/{courier_id}")
