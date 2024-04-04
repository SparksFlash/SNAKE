def increment(number, by):
    return number + by


print(increment(12, by=6))                 # Here by is called keyword argument


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="X", child2="Y", child3="Z")
