import requests


class APIClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url


    def send_get_request(self, url):
        print(f"Итоговый url = {url}")
        response = requests.get(url)
        return response


    def send_post_request(self, url, data):
        print(f"Итоговый url = {url}")
        response = requests.post(url, json=data)
        return response


    def send_put_request(self, url, data):
        print(f"Итоговый url = {url}")
        response = requests.put(url, json=data)
        return response


    def send_patch_request(self, url, data):
        print(f"Итоговый url = {url}")
        response = requests.patch(url, json=data)
        return response


    def send_delete_request(self, url):
        print(f"Итоговый url = {url}")
        response = requests.delete(url)
        return response
