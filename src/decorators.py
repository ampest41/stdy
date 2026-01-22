import time


def log(filename=None):
    '''функция декоратор записывающая результат в logfile или выводящая инфо в консоль'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as f:
                        message = f"{func.__name__} ok"
                        f.write(message + '\n')
                else:
                    message = f"{func.__name__} ok"
                    print(message)

                return result
            except Exception as e:
                error_type = type(e).__name__
                message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(message + '\n')
                else:
                    print(message)

                raise

        return wrapper
    return decorator
