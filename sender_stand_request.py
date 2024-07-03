import configuration
import data
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_track_number():
    response = post_new_order(data.order_body)
    return response.json()["track"]

def get_order_by_track():
    t = "?t="
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + t + str(get_track_number()))










