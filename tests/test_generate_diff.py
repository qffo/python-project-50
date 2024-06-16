from gendiff.generate_diff import generate_diff


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'

    assert generate_diff('tests/fixtures/file3.yaml',
                         'tests/fixtures/file4.json') == """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


assert generate_diff('tests/fixtures/file3.json',
                     'tests/fixtures/file4.json', 'plain') == """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

assert generate_diff('tests/fixtures/file3.json',
                     'tests/fixtures/file4.json', 'json') == """{
    "common": {
        "type": "nested",
        "value": {
            "follow": {
                "type": "added",
                "value": false
            },
            "setting1": {
                "type": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "type": "removed",
                "value": 200
            },
            "setting3": {
                "type": "changed",
                "old": true,
                "new": null
            },
            "setting4": {
                "type": "added",
                "value": "blah blah"
            },
            "setting5": {
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "type": "nested",
                "value": {
                    "doge": {
                        "type": "nested",
                        "value": {
                            "wow": {
                                "type": "changed",
                                "old": "",
                                "new": "so much"
                            }
                        }
                    },
                    "key": {
                        "type": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "type": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "type": "nested",
        "value": {
            "baz": {
                "type": "changed",
                "old": "bas",
                "new": "bars"
            },
            "foo": {
                "type": "unchanged",
                "value": "bar"
            },
            "nest": {
                "type": "changed",
                "old": {
                    "key": "value"
                },
                "new": "str"
            }
        }
    },
    "group2": {
        "type": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}"""
