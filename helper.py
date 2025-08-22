from generators import generate_order_data


def modify_order_data(key,value):
    body = generate_order_data()
    body[key] = value
    return body
