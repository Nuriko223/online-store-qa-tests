
import requests

def test_api_status():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
