from faker import Faker

fake = Faker()

def generate_fake_courier():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=10),
        "firstName": fake.first_name()
    }

def generate_order_data():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": str(fake.random_int(min=1, max=10)),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=10),
        "deliveryDate": fake.date_between(start_date="+1d", end_date="+30d").isoformat(),
        "comment": fake.text(max_nb_chars=100),
        "color": []
    }
