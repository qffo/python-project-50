import json


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    result = {}
    # print(f1, f2)
    for k, v in f1.items():
        print(f"f1{k, v}")
    for k, v in f2.items():
        print(f"f2{k, v}")
    return f1


print(generate_diff('files_for_test/file1.json', 'files_for_test/file2.json'))
