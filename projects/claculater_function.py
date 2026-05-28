def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

operator = input('enter operator(+,*,-,/): ')
a=float(input('enter first number: '))
b=float(input('enter second number: '))

if operator == '+':
    result=add(a,b)
    print(result)
elif operator=='-':
    result=sub(a,b)
    print(result)
elif operator=='*':
    result=mul(a,b)
    print(result)
elif operator=='/':
    result=div(a,b)
    print(result)
else:
    print('invalid value!')

        