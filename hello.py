def my_function(n):
    return lambda a: a * n

mytripler=my_function(3)
print(mytripler(4))