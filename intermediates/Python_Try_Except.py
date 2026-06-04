# try lets you to check block of code for error
#except lets you handle error
#else block lets you excute when their is no error
#finally clock that lets you excute code regardless of result of try -except blocks
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("You can't divide by zero")
else:   print("Division successful")
finally:    print("This will always execute")