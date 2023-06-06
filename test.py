def function1():
    return 42

def function2(value):
    result = value + 10
    print(result)

# Call function1 and assign its return value to a variable
returned_value = function1()

# Pass the returned value as an argument to function2
function2(returned_value)
