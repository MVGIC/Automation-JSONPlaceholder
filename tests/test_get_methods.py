import os.path
import utils.utils as u

from conftest import *

class TestGetMethods:
    RESOURCE_NAME = ["albums", "comments", "photos", "posts", "todos", "users"]

    @pytest.mark.parametrize("endpoint, expected_data",
                             [(x, u.open_json_file(os.path.join(os.path.dirname(__file__),
                                                                        f"resources/{x}/all_resources.json")))
                              for x in RESOURCE_NAME])

    def test_get_all_resources(self, api_client, endpoint, expected_data):
        print(endpoint) # название ресурса
        print(expected_data) # ожидаемые данные из JSON

        response = api_client.send_get_request(endpoint)
        assert response.status_code == 200
        assert response.json() is not None

#TODO: 1) продолжение - https://www.youtube.com/watch?v=AFuTzPWEYF4
#TODO: 2) понять что написали в лябмда функции (test_get_all_resources) / 2) Может удалить этот тест и написать простые другие?
#TODO: 3) улучшить проект фишками из учебного проекта 4) улучшить проект фишками из рабочего проекта 5) добавить проверки