#input() is function that allows us to get user input data and returns the entered data as string
name = input('what is your name?')
age = int(input('how old are you?'))
age = age + 1
print(f'you are {age} years old {name}')