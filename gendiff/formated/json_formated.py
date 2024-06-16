import json


def format_json(diff: dict) -> str:
    return json.dumps(diff, indent=4)
