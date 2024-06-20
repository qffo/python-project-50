import pytest
from gendiff.generate_diff import generate_diff

json_old = 'tests/fixtures/file3.json'
json_new = 'tests/fixtures/file4.json'
yaml_old = 'tests/fixtures/file3.yaml'
yaml_new = 'tests/fixtures/file4.yaml'

stylish = 'tests/fixtures/nested_stylish'
plain = 'tests/fixtures/nested_plain'
jsonn = 'tests/fixtures/json.json'


@pytest.mark.parametrize(
    'path1, path2, format_name, expected',
    [
        (json_old, json_new, 'stylish', stylish),
        (json_old, json_new, 'plain', plain),
        (json_old, json_new, 'json', jsonn),
        (yaml_old, yaml_new, 'stylish', stylish),
        (yaml_old, yaml_new, 'plain', plain),
        (yaml_old, yaml_new, 'json', jsonn),

    ]
)
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as expectation:
        assert generate_diff(path1, path2, format_name) == expectation.read()
