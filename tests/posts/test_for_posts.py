import allure
import pytest

from constants.url import BASE_URL
from schemas.post import *
from utils.checking import Checking


class TestForPosts:

    @allure.id("")
    @allure.title("")
    @pytest.mark.smoke
    def test_get_all_posts(self, get_all_posts_fixture):
        """

        :param get_all_posts_fixture:
        :return:
        """
        with allure.step(""):
            assert get_all_posts_fixture().assert_status_code(200).validate(PostBody)

    def test_send_new_post(self, api_client):
        url = f"{BASE_URL}/posts"
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
