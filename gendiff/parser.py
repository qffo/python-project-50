import json
import yaml


def parse(data: str, format: str):
    if format == 'json':
        return json.loads(data)
    elif format == 'yaml':
        return yaml.load(data, Loader=yaml.FullLoader) or {}
    raise ValueError("Неподдерживаемый формат файла")
