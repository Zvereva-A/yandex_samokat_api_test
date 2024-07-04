import sender_stand_request

# Анастасия Зверева, 18-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_by_track():
    response = sender_stand_request.get_order_by_track()

    assert response.status_code == 200




