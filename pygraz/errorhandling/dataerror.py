'''
Template for your own exceptions.
'''
import os


class DataErrorSimple(Exception):
    '''
    Example for an own Exception which simply inherits a basic constructor to
    specify an error message.
    '''
    pass

def testRaiseDataErrorSimple():
    height = -3
    raise DataErrorSimple('height is %d but must be greater than 0' % height)

class DataError(Exception):
    '''
    Example for an own Exception with its own constructor and instance
    variables. It also has its own `__str__` and related methods to show
    details about the exception. Furthermore there is a `__cmp__` to sort
    multiple exceptions, in this case by file name and location.
    '''
    def __init__(self, message, filePath, line=None, column=None):
        assert message is not None
        assert filePath is not None
        Exception.__init__(self, message)
        self._message = message
        self._filePath = filePath
        self._line = line
        self._column = column

    @property
    def filePath(self):
        return self._filePath

    @property
    def line(self):
        return self._line

    @property
    def column(self):
        return self._column

    def __unicode__(self):
        result = u"" + os.path.basename(self.filePath)
        if self.line is not None:
            result += u' (%d' % self.line
            if self.column is not None:
                result += u':%d' % self.column
            result += u')'
        result += u': %s' % self._message
        return result

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        assert other is not None
        if self.filePath == other.filePath:
            if self.line == other.line:
                result = cmp(self.column, other.column)
            else:
                result = cmp(self.line, other.line)
        else:
            result = cmp(self.filePath, other.filePath)
        return result

if __name__ == "__main__":
    # Exercise the new exceptions.
    try:
        raise DataErrorSimple('test: some data must be something else')
    except DataErrorSimple as error:
        print(error)

    try:
        raise DataError('test: some data must be something else',
            'some.txt', 5, 3)
    except DataError as error:
        print(error)

    try:
        raise DataError(u'test: some data must be something else',
            'some.txt', 5, 3)
    except DataError as error:
        print(error)
