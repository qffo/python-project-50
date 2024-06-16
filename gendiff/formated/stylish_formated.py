INDENT = 4


def make_value(data, depth: int):
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return 'null'
    if not isinstance(data, dict):
        return data
    result = '{'
    for key, val in data.items():
        result += f'\n{" " * (depth + 1) * INDENT}{key}:' \
            f' {make_value(val, depth + 1)}'
    result += f'\n{" " * depth * INDENT}}}'
    return result


def make_stylish_string(diff_dict: dict, depth: int) -> str:
    result = ''

    for key, val in diff_dict.items():
        match val.get('type'):
            case 'changed':
                result += f'{" " * depth * INDENT}' \
                    f'{" " * (INDENT - 2) + "- "}{key}:' \
                    f' {make_value(val["old"], depth + 1)}\n'
                result += f'{" " * depth * INDENT}' \
                    f'{" " * (INDENT - 2) + "+ "}{key}:' \
                    f' {make_value(val["new"], depth + 1)}\n'
            case 'nested':
                result += f'{" " * (depth + 1) * INDENT}{key}: {{\n' \
                    f'{make_stylish_string(val["value"], depth + 1)}' \
                    f'{" " * (depth + 1) * INDENT}}}\n'
            case 'removed':
                result += f'{" " * depth * INDENT}' \
                    f'{" " * (INDENT - 2) + "- "}{key}: ' \
                    f'{make_value(val["value"], depth + 1)}\n'
            case 'added':
                result += f'{" " * depth * INDENT}' \
                    f'{" " * (INDENT - 2) + "+ "}{key}: ' \
                    f'{make_value(val["value"], depth + 1)}\n'
            case _:
                result += f'{" " * (depth + 1) * INDENT}{key}: ' \
                    f'{make_value(val["value"], depth + 1)}\n'

    return result


def format_stylish(diff: dict) -> str:

    result = make_stylish_string(diff, 0)
    return f'{{\n{result}}}'
