from .parser import parse
import requests


def read_file(file_path):
    if file_path.startswith('http'):
        return network_data(file_path)

    with open(file_path, 'r') as file:
        if file_path.endswith('json'):
            return parse(file.read(), 'json')
        elif file_path.endswith('yaml') or file_path.endswith('yml'):
            return parse(file.read(), 'yaml')


def network_data(url):
    data = requests.get(url).text

    if url.endswith('json'):
        return parse(data, 'json')

    elif url.endswith('yaml') or url.endswith('yml'):
        return parse(data, 'yaml')
