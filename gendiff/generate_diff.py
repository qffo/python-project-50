from .parser_file import parsering
from collections import OrderedDict
from .formated.stylish_formated import format_stylish
from .formated.plain_formated import format_plain
from .formated.json_formated import format_json


def gen_diff(data1: dict, data2: dict) -> dict:  # noqa: C901
    diff = {}
    keys = set(data1.keys() | set(data2.keys()))

    for i in keys:
        if i not in data1.keys():
            diff[i] = {'type': 'added', 'value': data2[i]}
        if i not in data2.keys():
            diff[i] = {'type': 'removed', 'value': data1[i]}

        if i in data1.keys() and i in data2.keys():
            if isinstance(data1[i], dict) and isinstance(data2[i], dict):
                diff[i] = {'type': 'nested',
                           'value': gen_diff(data1[i], data2[i])}

            elif data1[i] == data2[i]:
                diff[i] = {'type': 'unchanged', 'value': data1[i]}

            else:
                diff[i] = {'type': 'changed', 'old': data1[i], 'new': data2[i]}

    return OrderedDict(sorted(diff.items(), key=lambda k: k))


def generate_diff(file_path1: str, file_path2: str, format='stylish'):
    old_file = parsering(file_path1)
    new_file = parsering(file_path2)
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


# print(generate_diff('tests/fixtures/file3.yaml', 'tests/fixtures/file4.json'))
# print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
