'''
Test performance of various error handling mechanisms.
'''
import time

VALID_NAME = 'bob'
NAME_TO_PHONE_MAP = {
    'alice': '0664/12345678',
    VALID_NAME: '0699/87654321',
    'joe': '0650/23456789',
    'sue': '0316/13245768'
}

MISSING_NAME = 'no such name'
REPETITIONS = 10000000
FAIL_EACH = 10


def nameForStep(step):
    if step % FAIL_EACH == 0:
        result = MISSING_NAME
    else:
        result = VALID_NAME
    return result


def timeForKeyError():
    startTime = time.clock()
    for step in xrange(REPETITIONS):
        try:
            x = NAME_TO_PHONE_MAP[nameForStep(step)]
        except KeyError:
            x = 'no number'
    return time.clock() - startTime


def timeForNoneHandler():
    startTime = time.clock()
    for step in xrange(REPETITIONS):
        x = NAME_TO_PHONE_MAP.get(nameForStep(step))
        if x is None:
            x = 'no number'
    return time.clock() - startTime


def timeForGet():
    startTime = time.clock()
    for step in xrange(REPETITIONS):
        x = NAME_TO_PHONE_MAP.get(nameForStep(step), 'no number')
    return time.clock() - startTime


if __name__ == '__main__':
    print('run time with KeyError: %.3fs' % timeForKeyError())
    print('run time with None handler: %.3fs' % timeForKeyError())
    print('run time with get(): %.3fs' % timeForKeyError())
