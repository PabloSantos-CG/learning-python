def sum(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a / b

def create_functions(fun, first_number):
    def closure(last_number):
        return fun(first_number, last_number)
    return closure

mock1 = create_functions(sum, 1998)
mock2 = create_functions(multiply, 1998)
mock3 = create_functions(divide, 1998)

print(mock1(10))
print(mock2(10))
print(mock3(10))