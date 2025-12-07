import json

def open_json_file(path:str)->list[dict]:
    """
    Открытие файла
    :param path: адрес файла для открытия
    :return:
    """
    with open(path) as json_file:
        data = json.load(json_file)
    return data