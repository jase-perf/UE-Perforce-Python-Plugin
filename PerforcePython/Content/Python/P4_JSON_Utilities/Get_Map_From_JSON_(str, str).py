"""
Execute Python Script Node:
Inputs:
- json_input: str

Outputs:
- data: Dict[str, str]
"""

import json

data = json.loads(json_input)

for key in data:
    data[key] = str(data[key])
