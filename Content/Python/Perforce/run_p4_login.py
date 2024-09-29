"""
Run p4 login with a provided password.

Execute Python Script Node:
Inputs:
- password: str
- p4user: str
- p4port: str
- p4client: str

Outputs:
- json_outputs: List[str]
- errors: List[str]
- success: bool
"""

import json
from P4 import P4, P4Exception

success = False

p4 = P4()
p4.user = p4user
p4.port = p4port
p4.client = p4client
p4.password = password

p4.connect()

try:
    res = p4.run_login()
    json_outputs = [json.dumps(item, indent=4) for item in res]
    errors = []
    success = True
except P4Exception as e:
    print(e)
    json_outputs = []
    errors = p4.errors
    success = False
