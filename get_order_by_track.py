import sender_stand_request
import data

# Анастасия Зверева, 18-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_by_track():
    order = sender_stand_request.post_new_order(data.order_body)
    track = order.json()["track"]
    get_order_by_track = sender_stand_request.get_order_by_track(track)

    assert get_order_by_track.status_code == 200




