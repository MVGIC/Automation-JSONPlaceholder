import requests

from constants.url import BASE_URL


class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def send_get_resources_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print(f"Итоговый url = {url}")
        response = requests.get(url, timeout=10)
        return response


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
