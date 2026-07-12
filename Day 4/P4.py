def add_two(x):
    return x+2
def subract_five(x):
    return x-5

def compose_functions(value):
    result = add_two(value)
    result = subract_five(result)
    return result

def compose(*functions):
    def composed_func(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return composed_func

pipeline = compose(add_two,subract_five)
print(pipeline(20))