"""
Execute Python Script Node:
Inputs:
- json_input: str

Outputs:
- value: List[str]
"""

import json

data = json.loads(json_input)


def get_keys():
    return list(data.keys())


value = get_keys()
