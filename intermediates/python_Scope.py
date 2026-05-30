# #Global variables are available from within any scope, global and local
# x=300
# def my_fun():
#     print(x)

# my_fun()

# print(x)
# #naming varibale: Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):


# def my_fun():
#     global x #we can use globale keyword
#     x=200
#     print(x)
# my_fun()
# print(x)

def countdown(n):
    if n<=0:
        print('done!')
    else:
        print(n)
        countdown(n-1)
countdown(5)


def factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*factorial(n-1)
print(factorial(8))
 