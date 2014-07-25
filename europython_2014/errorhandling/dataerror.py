"""
Template for your own exceptions.
"""
import os


class DataErrorSimple(Exception):
    """
    Example for an own Exception which simply inherits a basic constructor to
    specify an error message.
    """
    pass


class DataError(Exception):
    """
    Example for an own Exception with its own constructor and instance
    variables. It also has its own `__str__` and related methods to show
    details about the exception. Furthermore there is a `__cmp__` to sort
    multiple exceptions, in this case by file name and location.
    """
    def __init__(self, message, path, line=None, column=None):
        assert message is not None
        assert path is not None
        Exception.__init__(self, message)
        self._message = message
        self._path = path
        self._line = line
        self._column = column

    @property
    def path(self):
        return self._path

    @property
    def line(self):
        return self._line

    @property
    def column(self):
        return self._column

    def __str__(self):
        result = os.path.basename(self.path)
        if self.line is not None:
            result += ' (%d' % self.line
            if self.column is not None:
                result += ':%d' % self.column
            result += ')'
        result += ': %s' % self._message
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
