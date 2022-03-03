# import logging
# import time
import time


def logger(original_f):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_f.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_f(*args, **kwargs)

    return wrapper


def timer(original_f):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_f(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_f.__name__, t2))
        return result

    return wrapper


@timer
@logger
def display_info(pid, data):
    time.sleep(1)
    print('display_info ran with argeuments ({}, {})'.format(pid, data))


display_info('0x1', '600')