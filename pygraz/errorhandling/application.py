'''
Template for a Python application using solution oriented error handling.
'''
import logging
import optparse
import os
import sys

_log = logging.getLogger('some')


class DataError(ValueError):
    '''Error occurred during processing data.'''
    def __init__(self, filePath, line=None, column=None):
        assert filePath is not None
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


def _process(options, others):
    '''
    Process data specified in ``options`` and ``others``. If the data can not
    be processed, raise `DataError`.
    '''
    assert options is not None
    assert others is not None
    assert len(others) >= 1

    # Here we would normally process something.
    pass


def main(arguments=None):
    if arguments is None:
        arguments = sys.argv

    # Exit code: 0=success, >0=error.
    result = 1

    # Process arguments. In case of errors, report them and exit.
    parser = optparse.OptionParser(usage='process some report')
    parser.add_option("-o", "--out", dest="targetPath",
        help="write report to FILE", metavar="FILE")
    options, others = parser.parse_args(arguments)
    if len(others) < 1:
        # Note: parser.error() raises SystemExit.
        parser.error('input files must be specified')

    try:
        _process(options, others)
        result = 0  # Success!
    except KeyboardInterrupt:
        _log.error('stopped as requested by user')
    except (DataError, EnvironmentError) as error:
        _log.error(error)
    except Exception as error:
        _log.exception(error)
    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
