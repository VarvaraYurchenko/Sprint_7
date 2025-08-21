import pytest
import allure
from generators import generate_fake_courier
from methods.courier_methods import CourierMethods
from data import Message, TestData


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, create_and_delete_courier):
        login, password = create_and_delete_courier

        with allure.step('Отправить POST-запрос на авторизацию курьера'):
            response = CourierMethods.login_courier(login, password)

        with allure.step('Проверить, что статус-код 200 и успешный запрос возвращает id'):
            assert response.status_code == 200
            assert 'id' in response.json()
            assert isinstance(response.json()['id'], int)

    @allure.title('Нельзя авторизоваться без логина')
    def test_login_courier_without_login_error(self, delete_courier):
        with allure.step('Создать курьера'):
            courier_data = generate_fake_courier()
            login = courier_data['login']
            password = courier_data['password']

            create_response = CourierMethods.create_courier(courier_data)
            assert create_response.status_code == 201

            delete_courier.append((login, password))

        with allure.step('Отправить POST-запрос на авторизацию без логина'):
            response = CourierMethods.login_courier('', password)

        with allure.step('Проверить, что статус-код 400 и правильное сообщение об ошибке'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert response.json()['message'] == Message.LOGIN_COURIER_MISSING_FIELDS

    @allure.title('Нельзя авторизоваться без пароля')
    def test_login_courier_without_password_error(self, delete_courier):
        with allure.step('Создать курьера'):
            courier_data = generate_fake_courier()
            login = courier_data['login']
            password = courier_data['password']

            create_response = CourierMethods.create_courier(courier_data)
            assert create_response.status_code == 201

            delete_courier.append((login, password))

        with allure.step('Отправить POST-запрос на авторизацию без пароля'):
            response = CourierMethods.login_courier(login, '')

        with allure.step('Проверить, что статус-код 400 и правильное сообщение об ошибке'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert response.json()['message'] == Message.LOGIN_COURIER_MISSING_FIELDS

    @allure.title('Нельзя авторизоваться с несуществующим логином')
    def test_login_courier_invalid_login_error(self, create_and_delete_courier):
        _, password = create_and_delete_courier

        with allure.step('Отправить POST-запрос на авторизацию с несуществующим логином'):
            response = CourierMethods.login_courier(TestData.NONEXISTENT_LOGIN, password)

        with allure.step('Проверить, что статус-код 404 и правильное сообщение об ошибке'):
            assert response.status_code == 404
            response_data = response.json()
            assert 'message' in response_data
            assert response_data['message'] == Message.LOGIN_COURIER_NOT_FOUND

    @allure.title('Нельзя авторизоваться с несуществующим паролем')
    def test_login_courier_invalid_password_error(self, create_and_delete_courier):
        login, _ = create_and_delete_courier

        with allure.step('Отправить POST-запрос на авторизацию с несуществующим паролем'):
            response = CourierMethods.login_courier(login, TestData.NONEXISTENT_PASSWORD)

        with allure.step('Проверить, что статус-код 404 и правильное сообщение об ошибке'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert response.json()['message'] == Message.LOGIN_COURIER_NOT_FOUND
