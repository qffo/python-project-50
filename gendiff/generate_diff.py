import json
import yaml


def generate_diff(file_path1, file_path2, format=json):  # noqa: C901

    def diff_yml(file_path1, file_path2):
        f1 = yaml.load(open(file_path1), Loader=yaml.FullLoader) or {}
        f2 = yaml.load(open(file_path2), Loader=yaml.FullLoader) or {}
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

    def diff_json(file_path1, file_path2):
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

    if file_path1.endswith('json'):
        return diff_json(file_path1, file_path2)
    if file_path1.endswith('yml'):
        return diff_yml(file_path1, file_path2)


# print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
# print(generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml'))
