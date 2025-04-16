
import sender_stand_request 
import configuration
import requests
import data
import pytest

# Екатерина Слипченко, 28-я когорта — Финальный проект. Инженер по тестированию плюс
# Проверка, что код ответа равен 200, при получение заказа по его треку 

def test_order():

# Запрос на создание заказа.

   response_new_order = sender_stand_request.new_order()

# Сохранение номера трека заказа.

   track_order = response_new_order.json()['track']

# Запрос на получения заказа по треку заказа.

   response = sender_stand_request.test_order(track_order)

# Проверка, что код ответа равен 200.

   assert response.status_code == 200
