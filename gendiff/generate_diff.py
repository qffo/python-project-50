from .read_file import read_file
from collections import OrderedDict
from .formated.stylish_formated import format_stylish
from .formated.plain_formated import format_plain
from .formated.json_formated import format_json


def gen_diff(data1, data2) -> dict:
    diff = {}
    keys = set(data1.keys() | set(data2.keys()))

    for i in keys:
        if isinstance(data1.get(i), dict) and isinstance(data2.get(i), dict):
            diff[i] = {'type': 'nested',
                       'value': gen_diff(data1[i], data2[i])}
        elif i not in data1.keys():
            diff[i] = {'type': 'added', 'value': data2[i]}
        elif i not in data2.keys():
            diff[i] = {'type': 'removed', 'value': data1[i]}
        elif data1[i] == data2[i]:
            diff[i] = {'type': 'unchanged', 'value': data1[i]}
        else:
            diff[i] = {'type': 'changed', 'old': data1[i], 'new': data2[i]}

    return OrderedDict(sorted(diff.items(), key=lambda k: k))


def generate_diff(data1: str, data2: str, format='stylish'):
    old_file = read_file(data1)
    new_file = read_file(data2)
    diff = gen_diff(old_file, new_file)

    match format:
        case None:
            return format_stylish(diff)
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
