
import sender_stand_request 
import configuration
import requests
import data
import pytest

# Екатерина Слипченко, 28-я когорта — Финальный проект. Инженер по тестированию плюс
# Проверка, что код ответа равен 200, при получение заказа по его треку 
def test_order():  
   response = requests.get(configuration.URL_SERVICE + configuration.ORDERS + str(sender_stand_request.track_new_order()))
   assert response.status_code == 200
