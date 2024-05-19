import json


def generate_diff(file_path1, file_path2, format=json):
    f1 = json.load(open(file_path1))
    f2 = json.load(open(file_path2))
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


# return '{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'
# print(generate_diff('files_for_test/file1.json', 'files_for_test/file2.json'))
