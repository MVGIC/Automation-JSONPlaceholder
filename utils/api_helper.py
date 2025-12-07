import requests


class APIClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def send_get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print(f"Итоговый url = {url}")
        response = requests.get(url)
        return response
    
