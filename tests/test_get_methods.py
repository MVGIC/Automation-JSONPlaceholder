import os.path

import utils.utils as u
from conftest import *
from utils.checking import Checking


class TestGetMethods:
    RESOURCE_NAME = ["albums", "comments", "photos", "posts", "todos", "users"]

    @pytest.mark.parametrize("endpoint, expected_data",
                             [(x, u.open_json_file(os.path.join(os.path.dirname(__file__),
                                                                f"resources/{x}/all_resources.json")))
                              for x in RESOURCE_NAME])
    def test_get_all_resources(self, api_client, endpoint, expected_data):
        print(endpoint)  # название ресурса
        print(expected_data)  # ожидаемые данные из JSON

        url = f"https://jsonplaceholder.typicode.com/{endpoint}"
        response = api_client.send_get_request(url)
        Checking.check_status_code(response, 200)
        assert response.json() is not None

    # TODO: 1) улучшить проект фишками из рабочего проекта 2) добавить проверки (нужен Pydantic) 3) спрятать не нужные проекты в гит (можно?)

    def test_get_all_posts(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = api_client.send_get_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)


    def test_get_first_post(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = api_client.send_get_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title", "sunt aut facere repellat provident "
                                                      "occaecati excepturi optio reprehenderit")
        Checking.check_json_search_word_in_values(response, "body", "architecto")


    def test_get_first_post_comments(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts/1/comments"
        response = api_client.send_get_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["postId", "id", "name", "email", "body"])
        Checking.check_json_values(response, "name",
                                   "alias odio sit")
        Checking.check_json_search_word_in_values(response, "body", "harum")

    # TODO: 1) нужны методы проверки значений по response

    def test_send_new_post(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts"
        new_post = {
            "userId": 13,
            "id": 1337,
            "title": "new magic post",
            "body": "test magic body"
        }
        response = api_client.send_post_request(url, new_post)
        print(response.json())
        Checking.check_status_code(response, 201)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title",
                                   "new magic post")
        Checking.check_json_search_word_in_values(response, "body", "body")


    def test_change_first_post(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        new_body = {
            "userId": 2,
            "id": 1,
            "title": "new title",
            "body": "new body"
        }
        response = api_client.send_put_request(url, new_body)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title",
                                   "new title")
        Checking.check_json_search_word_in_values(response, "body", "new body")


    def test_change_only_title_for_first_post(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        new_title = {
            "title": "changed only title"
        }
        response = api_client.send_patch_request(url, new_title)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title",
                                   "changed only title")


    def test_delete_first_post(self, api_client):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = api_client.send_delete_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        assert response.json() == {}
