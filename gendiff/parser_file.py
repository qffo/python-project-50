import json
import yaml


def parsering(file_path: str) -> dict:
    with open(file_path) as file:
        if file_path.endswith('json'):
            return json.load(file)  # Возвращает распарсенный JSON словарь
        if file_path.endswith('yml') or file_path.endswith('yaml'):
            # Возвращает распарсенный YAML словарь
            return yaml.load(file, Loader=yaml.FullLoader) or {}
    raise ValueError("Неподдерживаемый формат файла")
