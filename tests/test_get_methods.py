import os.path

import pytest

import utils.utils as u
from conftest import api_client
from constants.url import BASE_URL
from utils.checking import Checking


class TestGetMethods:
    RESOURCE_NAME = ["albums", "posts", "users"] # Проверяем ресурсы, которые успевают загружаться

    @pytest.mark.parametrize("endpoint", RESOURCE_NAME)
    def test_get_all_resources(self, api_client, endpoint):
        # Формируем путь к файлу с тестовыми данными
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_dir, "resources", endpoint, "all_resources.json")

        # Проверяем существование файла
        assert os.path.exists(json_file_path), f"Файл не найден: {json_file_path}"

        # Загружаем ожидаемые данные
        expected_data = u.open_json_file(json_file_path)

        print(f"\nТестируемый ресурс: {endpoint}")
        print(f"Путь к файлу: {json_file_path}")
        print(f"Ожидаемые данные загружены: {len(expected_data) if isinstance(expected_data, list) else 'N/A'} записей")

        # Выполняем запрос
        response = api_client.send_get_resources_request(endpoint)

        # Проверки
        Checking.check_status_code(response, 200)
        assert response.json() is not None, "Ответ API пустой"

        # Дополнительная проверка на соответствие данным
        actual_data = response.json()
        assert actual_data == expected_data, f"Данные не совпадают для ресурса {endpoint}"



    def test_get_first_post(self, api_client):
        url = f"{BASE_URL}/posts/1"
        response = api_client.send_get_request(url)
        print(response.json())
        Checking.check_status_code(response, 200)
        Checking.check_json_fields(response, ["userId", "id", "title", "body"])
        Checking.check_json_values(response, "title", "sunt aut facere repellat provident "
                                                      "occaecati excepturi optio reprehenderit")
        Checking.check_json_search_word_in_values(response, "body", "architecto")
