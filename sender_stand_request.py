import configuration
import data
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_order_by_track(track):
    t = "?t="
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + t + str(track))










