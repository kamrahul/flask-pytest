from  apps.factory import create_app


def test_new_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/dummy_module/print' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/dummy_module/print')
    assert response.status_code == 200


