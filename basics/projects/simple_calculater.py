operator = input( 'enter operator: ')
num1 = float(input('enter the frist number: '))
num2 = float(input('enter the second number: '))
if operator == '+':
    print(f'the sum of{num1} + {num2} is: {num1+num2}')
elif operator == '-':
    print(f'the sum of{num1} - {num2} is: {num1-num2}')
elif operator == '*':
    print(f'the sum of{num1} * {num2} is: {num1*num2}')
elif operator == '/':
    print(f'the sum of{num1} / {num2} is: {num1/num2}')
elif operator == '%':
    print(f'the sum of {num1} % {num2} is: {num1%num2}')
else: 
    print('invalid operator!')




