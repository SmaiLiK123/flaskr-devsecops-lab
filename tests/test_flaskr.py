import pytest
from flaskr import create_app

@pytest.fixture
def client():
    """Фикстура для создания тестового клиента Flask"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Flaskr' in response.data

def test_index_with_name(client):
    """Тест главной страницы с параметром name"""
    response = client.get('/?name=World')
    assert response.status_code == 200
    assert b'World' in response.data