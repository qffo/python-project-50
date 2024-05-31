import json
from .parser_file import parsering
from .ploskie import gen_dif_ploskie


def generate_diff(file_path1, file_path2, format=json):  # noqa: C901
    f1 = parsering(file_path1)
    f2 = parsering(file_path2)
    # проверяем, если файлы плоские,
    # то выпоняем функция для сравнения плоских файлов
    for _, v in f1.items():
        if not isinstance(v, dict):
            return gen_dif_ploskie(f1, f2)

    result_fn = []
    bar = ''

    def iter_solo(file_x):
        if not isinstance(file_x, dict):
            # print(file_x)
            return file_x

        result = []
        foo = ''
        # print(file_x)
        for k, v in file_x.items():
            # if isinstance(v, dict):
            # print(v)
            result.append((k, iter_solo(v)))

        for k, v in result:
            foo += f"            {str(k)}: {str(v)}\n"
        return f"{'{'}\n{foo}{'       }'}"

    def iter(file1, file2):
        if not isinstance(file1, dict):
            # print(file_x)
            return file1
        result = []
        foo = ''
        keys = set(file1.keys()) | set(file2.keys())
        # print(keys)
        for i in keys:
            if i in file1 and i in file2:
                result.append(f"  {i}: {(file1.get(i), file2.get(i))}")
            if i in file1 and i not in file2:
                result.append(f"- {i}: {file1[i]}")
            if i in file2 and i not in file1:
                result.append(f"+ {i}: {iter_solo(file2[i])}")

        result = sorted(result, key=lambda x: x[5:])
        for i in result:
            foo += f"  {str(i)}\n"
        print(foo)

        # for k, v in file1.items():
        #     if file1.get(k) == file2.get(k):
        #         result.append(('', k, v))
        #     if file1.get(k) != file2.get(k):
        #         result.append(('-', k, v))
        # for k, v in file2.items():
        #     if file2.get(k) != file1.get(k):
        #         result.append(('+', k, iter_solo(v)))
        # result = sorted(result, key=lambda x: x[1])
        # for i, k, v in result:
        #     if i != '-' and i != '+':
        #         foo += f'       {str(i)} {str(k)}: {(str(v)).lower()}\n'
        #     else:
        #         foo += f'      {str(i)} {str(k)}: {(str(v)).lower()}\n'
        # return f"{'{'}\n{foo}{'    }'}"

    # def iter(file1, file2):
    #     result = []
    #     foo = ''
    #     for k, v in file1.items():
    #         if file1.get(k) == file2.get(k):
    #             result.append(('', k, v))
    #         if file1.get(k) != file2.get(k):
    #             result.append(('-', k, v))
    #     for k, v in file2.items():
    #         if file2.get(k) != file1.get(k):
    #             result.append(('+', k, iter_solo(v)))
    #     result = sorted(result, key=lambda x: x[1])
    #     for i, k, v in result:
    #         if i != '-' and i != '+':
    #             foo += f'       {str(i)} {str(k)}: {(str(v)).lower()}\n'
    #         else:
    #             foo += f'      {str(i)} {str(k)}: {(str(v)).lower()}\n'
    #     return f"{'{'}\n{foo}{'    }'}"

    # def iter_(current_value):
    #     if isinstance(current_value, dict):
    #         print(current_value)

    keys = set(f1.keys()) | set(f2.keys())
    for i in keys:
        if i in f1 and i in f2:
            result_fn.append(f"  {i}: {iter(f1.get(i), f2.get(i))}")
        if i in f1 and i not in f2:
            result_fn.append(f"- {i}: {f1[i]}")
        if i in f2 and i not in f1:
            result_fn.append(f"+ {i}: {iter_solo(f2[i])}")

    result_fn = sorted(result_fn, key=lambda x: x[5:])
    # result_fn = sorted(result_fn)
    for i in result_fn:
        bar += f"  {str(i)}\n"
    # print(f"{'{'}\n{bar}{'}'}")
    # return f"{'{'}\n{bar}{'}'}"


print(generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json'))
# print(generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml'))
