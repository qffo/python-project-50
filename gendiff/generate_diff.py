import json
from .parser_file import parsering
from .ploskie import gendif_ploskie
from .iter_solo import iter_solo


def generate_diff(file_path1, file_path2, format=json):  # noqa: C901
    f1 = parsering(file_path1)
    f2 = parsering(file_path2)
    # проверяем, если файлы плоские,
    # то выпоняем функция для сравнения плоских файлов
    for _, v in f1.items():
        if not isinstance(v, dict):
            return gendif_ploskie(f1, f2)

    result = []
    foo = ''

    def iter(x, y):
        result = []
        foo = ''
        keys = set(x.keys()) | set(y.keys())
        for i in keys:
            if i in x and i not in y:
                if not isinstance(x.get(i), dict):
                    result.append(f"    - {i}: {x.get(i)}")
            if i not in x and i in y:
                if not isinstance(y.get(i), dict):
                    result.append(f"    + {i}: {y.get(i)}")
            if i in x and i in y:
                if x.get(i) == y.get(i):
                    result.append(f"      {i}: {x.get(i)}")
            if i in x and i in y:
                if x.get(i) != y.get(i):
                    if not isinstance(x.get(i), dict):
                        result.append(f"    - {i}: {x.get(i)}")
                        result.append(f"    + {i}: {y.get(i)}")
                    if isinstance(x.get(i), dict):
                        result.append(f"      {i}: {x.get(i)}")

        for i in sorted(result, key=lambda x: x[8]):
            foo += f"  {str(i.lower())}\n"

        return f"{'{'}\n{foo}{'    }'}"

    keys = set(f1.keys()) | set(f2.keys())
    for i in keys:
        if i in f1 and i in f2:
            result.append(f"  {i}: {iter(f1.get(i), f2.get(i))}")
        if i in f1 and i not in f2:
            result.append(f"- {i}: {iter_solo(f1[i])}")
        if i in f2 and i not in f1:
            result.append(f"+ {i}: {iter_solo(f2[i])}")

    result = sorted(result, key=lambda x: x[5:])
    for i in result:
        foo += f"  {str(i)}\n"

    return f"{'{'}\n{foo}{'}'}"


# print(generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json'))
# print(generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml'))
