# def walk(steps):
#     if steps == 0:
#         print('you have reached your destination')
#         return
#     print(f'you take step #{steps}')
#     walk(steps -1)

# walk(50)
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
