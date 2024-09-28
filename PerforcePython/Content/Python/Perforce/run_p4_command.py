"""
Run a command with p4.run() and return results as an array of json strings.

Execute Python Script Node:
Inputs:
- command: str
- arguments: List[str]
- p4user: str
- p4port: str
- p4client: str
- project_dir: str

Outputs:
- json_output: str (The full output in json format)
- json_outputs: List[str] (An array of each item in json format)
- errors: List[str]
- success: bool
"""

import os
import json
from P4 import P4, P4Exception

success = False

os.chdir(project_dir)

p4 = P4()
p4.user = p4user
p4.port = p4port
p4.client = p4client
try:
    p4.connect()
except:
    errors = p4.errors
    print(p4.errors)
try:
    res = p4.run(command, *arguments)
    json_output = json.dumps(res, indent=4)
    json_outputs = [json.dumps(item, indent=4) for item in res]
    errors = []
    success = True
except P4Exception as e:
    print(e)
    json_output = "[]"
    json_outputs = []
    errors = p4.errors
    success = False
