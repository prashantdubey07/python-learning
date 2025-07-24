# Python code​​​​​​‌‌​‌‌‌​​​‌​‌​​‌‌‌‌​‌​‌‌‌​ below
def handleNonIntArguments(func):
    def wrapper(*args):
        try:
            for arg in args: 
                if type(arg) is not int:
                    raise NonIntArgumentException()
            return func(*args)
        finally:
            pass
    return wrapper

class NonIntArgumentException(Exception):
    pass
