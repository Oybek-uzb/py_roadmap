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

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {} and kwargs: {}".format(args, kwargs)
        )

        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info_2(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info_2("Oybek", 20)

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1

        print("{} ran in : {} sec".format(orig_func.__name__, t2))
        
        return result
        
    return wrapper

@my_timer
def display_info_3(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info_3("Oybek", 21)