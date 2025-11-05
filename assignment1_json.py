"""
    This is for Assignment API: 1.3 JSON - our new friend
"""

import json

with open("json_assignment1/example7_assignment.json", "r") as file:
    data = json.load(file)

print(f"Email of second student in first CS course: {data['school']['departments'][0]['courses'][0]['students'][1]['email']}")
print(f"Office room of CS department head: {data['school']['departments'][0]['head']['office']['room']}")
print(f"First review comment of first book: {data['school']['library']['books'][0]['reviews'][0]['comment']}")
print(f"Price of second book: {data['school']['library']['books'][1]['price']}")
print(f"Building for second event: {data['school']['events'][1]['location']['building']}")

