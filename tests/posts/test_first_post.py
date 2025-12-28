import allure

from conftest import *
from constants.url import BASE_URL
from utils.checking import Checking


class TestForFirstPost:

    @allure.id("5")
    @allure.title("Проверка изменения первого поста")
    @pytest.mark.smoke
    @pytest.mark.api
    def test_change_first_post(self, api_client):
        url = f"{BASE_URL}/posts/1"
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


    @allure.id("6")
    @allure.title("Проверка изменения только заголовка первого поста")
    @pytest.mark.smoke
    @pytest.mark.api
    def test_change_only_title_for_first_post(self, api_client):
        url = f"{BASE_URL}/posts/1"
        new_title = {
            "title": "changed only title"
        }
        response = api_client.send_patch_request(url, new_title)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title",
                                   "changed only title")


    @allure.id("7")
    @allure.title("Проверка удаления первого поста")
    @pytest.mark.smoke
    @pytest.mark.api
    def test_delete_first_post(self, api_client):
        url = f"{BASE_URL}/posts/1"
        response = api_client.send_delete_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        assert response.json() == {}
