"""
Execute Python Script Node:
Inputs:
- json_input: str
- key: str

Outputs:
- value: float
"""

import json

data = json.loads(json_input)


def get_value(key: str):
    try:
        return float(data.get(key))
    except TypeError:
        return None


value = get_value(key)

if value is None:
    error_message = (
        f"Key '{key}' does not exist or '{data.get(key)}' cannot be cast to Float"
    )
    print(error_message)
    raise ValueError(error_message)
