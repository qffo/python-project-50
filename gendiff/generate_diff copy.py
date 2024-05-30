import json
from parser_file import parsering


def generate_diff(file_path1, file_path2, format=json):  # noqa: C901
    f1 = parsering(file_path1)
    f2 = parsering(file_path2)
    result = []
    foo = ''
    for k, v in f1.items():
        if f1.get(k) == f2.get(k):
            result.append(('', k, v))
        if f1.get(k) != f2.get(k):
            result.append(('-', k, v))
    for k, v in f2.items():
        if f2.get(k) != f1.get(k):
            result.append(('+', k, v))
    result = sorted(result, key=lambda x: x[1])
    for i, k, v in result:
        if i != '-' and i != '+':
            foo += f'   {str(i)} {str(k)}: {(str(v)).lower()}\n'
        else:
            foo += f'  {str(i)} {str(k)}: {(str(v)).lower()}\n'
    return f"{'{'}\n{foo}{'}'}"


print(generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json'))
# print(generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml'))
