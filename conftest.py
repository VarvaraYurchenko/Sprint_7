import pytest
from generators import generate_fake_courier
from methods.courier_methods import CourierMethods


@pytest.fixture
def create_and_delete_courier():
    courier_data = generate_fake_courier()
    login = courier_data['login']
    password = courier_data['password']

    CourierMethods.create_courier(courier_data)

    yield login, password

    login_response = CourierMethods.login_courier(login, password)
    courier_id = login_response.json().get('id', None)

    if courier_id is not None:
        CourierMethods.delete_courier(courier_id)


@pytest.fixture
def delete_courier():
    created_credentials = []
    yield created_credentials
    for login, password in created_credentials:
        login_response = CourierMethods.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json().get('id')
            if courier_id:
                CourierMethods.delete_courier(courier_id)
