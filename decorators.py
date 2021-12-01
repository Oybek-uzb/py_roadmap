def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print("display function ran")

decorated_function = decorator_function(display)
decorated_function()

@decorator_function
def display_2():
    print("display_2 function ran")

# code in the lines 14-16 is equal to code in the lines 8-11

@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info("Oybek", "20")
# display_2()