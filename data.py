class URL:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru' # сайт Самокат

    CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'  # POST - создание курьера
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier' # DELETE - удаление курьера
    LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login' # POST - логин курьера в системе

    CREATE_ORDER_URL = f'{BASE_URL}/api/v1/orders' # POST - создание заказа
    GET_ORDERS_URL = f'{BASE_URL}/api/v1/orders' # GET - получение списка заказов

class Message:
    # Ошибки при создании курьера
    CREATE_COURIER_MISSING_FIELDS = "Недостаточно данных для создания учетной записи"
    CREATE_COURIER_ALREADY_EXISTS = "Этот логин уже используется"

    # Ошибки при логине
    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"
    LOGIN_COURIER_MISSING_FIELDS = "Недостаточно данных для входа"
