import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y['age'])

#Convert from Python to JSON

import json

x= {
    "name":"bacha",
    "age": 24,
    "city": "new York"
}

y = json.dumps(x)

print(y)
print(json.dumps({"name": "John", "age": 30}))

#example
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y=json.dumps(x)
print(y)