#Generators are functions that can pause and resume their execution.
#Generators allow you to iterate over data without storing the entire dataset in memory.
#Instead of using return, generators use the yield keyword. 
import mymodule as md
import platform as plt
import datetime as dt


def count_up_to(n):
    count = 1
    while count <=n:
        yield count
        count +=1
for num in count_up_to(5):
    print(num)



#To create a module just save the code you want in a file with the file extension .py:
md.greeting("Jonathan")
a = md.person1["age"]
print(a)
b=md.x
print(b)
print(plt.system())
print(dt.datetime.now())