# def gen_dif_ploskie(file1, file2):
#     result = []
#     foo = ''
#     for k, v in file1.items():
#         if file1.get(k) == file2.get(k):
#             result.append((' ', k, v))
#         if file1.get(k) != file2.get(k):
#             result.append(('-', k, v))
#     for k, v in file2.items():
#         if file2.get(k) != file1.get(k):
#             result.append(('+', k, v))
#     result = sorted(result, key=lambda x: x[1])
#     for i, k, v in result:
#         foo += f'  {str(i)} {str(k)}: {(str(v)).lower()}\n'
#     return f"{'{'}\n{foo}{'}'}"


def gen_dif_ploskie(file1, file2):
    result = []

    for k, v in file1.items():
        if file1.get(k) == file2.get(k):
            result.append((' ', k, v))
        elif file1.get(k) != file2.get(k):
            result.append(('-', k, v))

    for k, v in file2.items():
        if file2.get(k) != file1.get(k):
            result.append(('+', k, v))

    result = sorted(result, key=lambda x: x[1])

    formatted_result = '\n'.join(
        [f'  {i} {k}: {str(v).lower()}' for i, k, v in result])

    return f'{{\n{formatted_result}\n}}'
