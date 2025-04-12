import configuration
import requests
import data

# Создание заказа и получение его номера  
def track_new_order():  
    new_order_response = requests.post(configuration.URL_SERVICE + configuration.NEW_ORDERS,
                         json=data.new_orders_body)

    order_track = new_order_response.json()['track']
    return order_track
