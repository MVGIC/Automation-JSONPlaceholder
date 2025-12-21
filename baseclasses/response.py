import json


class Response:

    def __init__(self, response):
        self.parsed_object = None
        self.parsed_objects = []
        self.response = response
        self.response_json = response.json() if response.text else {}
        self.response_status = response.status_code

    @staticmethod
    def response_json(response):
        if response.text == '' and response.status_code == 200:
            return json.dumps(response.text)
        else:
            return response.json()
# TODO: 1) Возможно вообще не нужен

    def validate_and_get_json_value(self, schema):
        if isinstance(self.response_json, list):
            return [schema.model_validate(item) for item in self.response_json]
        else:
            return schema.model_validate(self.response_json)



    def validate(self, schema):
        if isinstance(self.response_json, list):
            self.parsed_objects = [] # Сохраняем ВСЕ валидированные объекты
            for item in self.response_json:
                parsed_object = schema.model_validate(item)
                self.parsed_objects.append(parsed_object)
        else:
            # Сохраняем одиночный объект
            self.parsed_object = schema.model_validate(self.response_json)

        return self

    def validate_get_value(self, schema, key_element):
        # Извлекаем значение один раз
        value = self.response_json.get(key_element)
        # Проверка на отсутствие ключа
        if value in None:
            raise KeyError(f"Ключ '{key_element}' не найден в response_json")
        # Обработка списка
        if isinstance(value, list):
            self.parsed_objects = [] # Сохраняем ВСЕ валидированные объекты
            for item in value:
                parsed_object = schema.model_validate(item)
                self.parsed_objects.append(parsed_object)
        else:
            self.parsed_object = schema.model_validate(value)

        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Request url: {self.response.url} \n" \
            f"Response body: {json.dumps(self.response_json, indent=4, sort_keys=True, ensure_ascii=False)}"
