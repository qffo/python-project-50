import json


def generate_diff(file_path1, file_path2):
    f1 = json.load(open(file_path1))
    f2 = json.load(open(file_path2))
    return f1, f2


print(generate_diff('files_for_test/file1.json', 'files_for_test/file2.json'))
