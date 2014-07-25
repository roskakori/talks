"""
Test performance of various error handling mechanisms.
"""
import random
import string
import time


def _name_to_number_map():
    result = {}
    random.seed(0)
    for _ in range(10):
        name = ''.join([
            random.choice(string.ascii_lowercase) for _ in range(10, random.randint(10, 20))
        ])
        result[name] = random.randint(0, 999999)
    return result

NAME_TO_PHONE_MAP = _name_to_number_map()
VALID_NAME = list(NAME_TO_PHONE_MAP.keys())[0]

MISSING_NAME = 'no such name'
REPETITIONS = 10000000
FAIL_EACH = 10


def name_for_step(step):
    if step % FAIL_EACH == 0:
        result = MISSING_NAME
    else:
        result = VALID_NAME
    return result


def time_for_key_error():
    startTime = time.clock()
    for step in range(REPETITIONS):
        try:
            x = NAME_TO_PHONE_MAP[name_for_step(step)]
        except KeyError:
            x = 'no number'
    return time.clock() - startTime


def time_for_none_handler():
    startTime = time.clock()
    for step in range(REPETITIONS):
        x = NAME_TO_PHONE_MAP.get(name_for_step(step))
        if x is None:
            x = 'no number'
    return time.clock() - startTime


def time_for_get_with_default():
    startTime = time.clock()
    for step in range(REPETITIONS):
        x = NAME_TO_PHONE_MAP.get(name_for_step(step), 'no number')
    return time.clock() - startTime


if __name__ == '__main__':
    print('run time with KeyError: %.3fs' % time_for_key_error())
    print('run time with None handler: %.3fs' % time_for_key_error())
    print('run time with get(): %.3fs' % time_for_key_error())
