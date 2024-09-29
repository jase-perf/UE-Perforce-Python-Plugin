"""
Check if server can be reached and if user is logged in.

Execute Python Script Node:
Inputs:
- p4user: str
- p4port: str
- p4client: str

Outputs:
- is_logged_in: bool
- ticket_duration_seconds: int
- errors: List[str]
"""

import json
from P4 import P4, P4Exception

is_logged_in = False
ticket_duration_seconds = 0
ticket_duration_

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
    res = p4.run("login", "-s")
    is_logged_in = True
    ticket_duration_seconds = res[0]["TicketExpiration"]
except P4Exception as e:
    print(e)
    errors = p4.errors
    is_logged_in = False
