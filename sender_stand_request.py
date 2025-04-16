import configuration
import requests
import data

# Создание заказа  
def new_order():  
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDERS,
                         json=data.new_orders_body)



# Получение заказа по его треку
def test_order(order_track):  
    return  requests.get(configuration.URL_SERVICE + configuration.ORDERS + str(order_track))
    
