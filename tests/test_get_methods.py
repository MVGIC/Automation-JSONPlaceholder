import os.path

import pytest

import utils.utils as u
from conftest import api_client
from constants.url import BASE_URL
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

        url = f"{BASE_URL}/{endpoint}"
        response = api_client.send_get_request(url)
        Checking.check_status_code(response, 200)
        assert response.json() is not None

    # TODO:
    #  1) коммиты
    #  2) requirements
    #  3) подключить CI/CD
    #  4) Сделать readme
    #  5) спрятать ненужные проекты в гит


    def test_get_first_post(self, api_client):
        url = f"{BASE_URL}/posts/1"
        response = api_client.send_get_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title", "sunt aut facere repellat provident "
                                                      "occaecati excepturi optio reprehenderit")
        Checking.check_json_search_word_in_values(response, "body", "architecto")
