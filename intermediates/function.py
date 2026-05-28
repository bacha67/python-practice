#Default Parameter Values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!


#Keyword Arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet(name="Bob", greeting="Hi"))  # Output: Hi, Bob!


#Positional Arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Charlie", "Hey"))  # Output: Hey, Charlie!


#Mixing Positional and Keyword Arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Dave", greeting="Welcome"))  # Output: Welcome, Dave!

#Passing Different Data Types
def process_data(data):
    if isinstance(data, list):
        return [x * 2 for x in data]
    elif isinstance(data, dict):
        return {k: v * 2 for k, v in data.items()}
    else:
        return f"Unsupported data type: {type(data)}"

print(process_data([1, 2, 3]))  # Output: [2, 4, 6]
print(process_data({'a': 1, 'b': 2}))  # Output: {'a': 2, 'b': 4}
print(process_data("Hello"))  # Output: Unsupported data type: <class 'str'>


#Returning Different Data Types
def calculate(value):
    if value > 0:
        return value * 2
    elif value < 0:
        return f"Negative value: {value}"
    else:
        return None

print(calculate(5))   # Output: 10
print(calculate(-3))  # Output: Negative value: -3
print(calculate(0))   # Output: None


#Default Parameter Values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
