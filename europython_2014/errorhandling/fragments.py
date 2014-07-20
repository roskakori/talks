'''
Various code fragments used in the slides. Keeping the original here helps
ensuring that the code is valid.
'''
import codecs
import logging
import sys

from dataerror import DataError

logging.basicConfig(level=logging.INFO)


# Dummy exception.
class SomeError(Exception):
    pass


def processSomething(height):
    if height <= 0:
        raise ValueError('height must be greater than 0')

    # Actual processing would happen here.
    pass


def processSomethingAgain(height):
    if height <= 0:
        raise ValueError(
            'height is %d ' % height
            + 'but must be greater than 0')

_log = logging.getLogger('some')


def processAllThings(dataFile):
    assert dataFile is not None

    lineNumber = 1
    try:
        # Process all heights read from `dataFile`.
        for lineNumber, line in enumerate(dataFile, start=1):
            processSomething(long(line))
    except ValueError as error:
        print('cannot process %s, line %d: %s' %
            (dataFile.name, lineNumber, error))


def reportExampleError():
    try:
        processSomething(-3)
    except ValueError as error:
        print error


# Dummy method.
def doSomething():
    raise SomeError('something must be something else')


def detectErrorAndRaiseException():
    actualValue = 1
    expectedValue = 2

    # Detect an error and raise an Exception.
    if actualValue != expectedValue:
        raise SomeError('helpful error message')


def processInput(inputFile):
    # Dummy
    pass


def cleanupWithFinally():
    # Using finally
    inputFile = codecs.open('some.txt', 'r', 'utf-8')
    try:
        processInput(inputFile)
    finally:
        inputFile.close()


def cleanupWithWith():
    with codecs.open('some.txt', 'r', 'utf-8') as inputFile:
        processInput(inputFile)


def cleanupWithClosing():
    def prepareCustomerDb():
        import sqlite3
        from contextlib import closing

        with closing(sqlite3.connect(':memory:')) as customerDb:
            with closing(customerDb.cursor()) as customerCursor:
                customerCursor.execute('''
                    create table customers
                        id integer,
                        first_name varchar(60),
                        last_name varchar(60),
                        date_of_birth datetime
                        primary key (id)
                ''')

    prepareCustomerDb()

    import sqlite3
    from contextlib import closing

    # Print all customers.
    with closing(sqlite3.connect(':memory:')) as customerDb:
        with closing(customerDb.cursor()) as customerCursor:
            for row in customerCursor('select * from customers'):
                print row


def processAllThingsPossiblyRaisingDataError(dataFile):
    assert dataFile is not None

    lineNumber = 1
    try:
        # Process all heights read from `dataFile`.
        for lineNumber, line in enumerate(dataFile, start=1):
            processSomething(long(line))
    except ValueError as error:
        raise DataError(dataFile.name, lineNumber, error)


def handleExceptionByLogging():
    # Handle an exception raised by a called routine.
    try:
        doSomething()
    except SomeError, error:
        logging.error(u'cannot do something: %s', error)


def reraiseExceptionWithOriginalStack():
    # Pass on an exception raised by a called routine and add context to the
    # error message.
    try:
        doSomething()
    except SomeError, error:
        raise sys.exc_info()[0], \
            SomeError(u'cannot do something: %s' % error), \
            sys.exc_info()[2]
        # raise sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]

if __name__ == '__main__':
    try:
        detectErrorAndRaiseException()
    except SomeError:
        pass

    handleExceptionByLogging()

#    reraiseExceptionWithOriginalStack()
    try:
        reraiseExceptionWithOriginalStack()
    except SomeError, error:
        logging.info(u'handled error: %s', error)

    reportExampleError()
