"""
Read the json output from fstat and output lists of added, modified, and deleted files.

Execute Python Script Node:
Inputs:
- json_input: str (The full output in json format)

Outputs:
- added_files: List[str]
- modified_files: List[str]
- deleted_files: List[str]
"""

import json

fstat = json.loads(json_input)

added_files = []
modified_files = []
deleted_files = []

for file in fstat:
    have = file.get("haveRev", "0")
    head = file.get("headRev")
    action = file.get("headAction")
    if not head:
        # File not in revision control yet
        continue
    if have != head:
        if "add" in action:
            added_files.append(file["clientFile"].replace("\\", "/"))
        elif "delete" in action:
            if have != "0":
                deleted_files.append(file["clientFile"].replace("\\", "/"))
        else:
            modified_files.append(file["clientFile"].replace("\\", "/"))
