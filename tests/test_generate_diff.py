import pytest
from gendiff.generate_diff import generate_diff

yml_file1 = 'tests/fixtures/file1.yml'
yaml_file2 = 'tests/fixtures/file2.yaml'

file3 = 'tests/fixtures/file3.json'
file4 = 'tests/fixtures/file4.json'

linear = 'tests/fixtures/linear'
stylish = 'tests/fixtures/nested_stylish'
plain = 'tests/fixtures/nested_plain'


@pytest.mark.parametrize(
    'path1, path2, format_name, expected',
    [
        (yml_file1, yaml_file2, 'stylish', linear),
        (file3, file4, 'stylish', stylish),
        (file3, file4, 'plain', plain),
    ]
)
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as expectation:
        assert generate_diff(path1, path2, format_name) == expectation.read()
