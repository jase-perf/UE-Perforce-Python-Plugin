"""
Execute Python Script Node:
Inputs:
- json_input: str
- key: str

Outputs:
- value: str
"""

import json

data = json.loads(json_input)


def get_value(key: str):
    return str(data.get(key))


value = get_value(key)

if value is None:
    error_message = f"Key '{key}' does not exist"
    print(error_message)
    raise ValueError(error_message)
