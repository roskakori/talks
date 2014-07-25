"""
Template for a Python application using solution oriented error handling.
"""
import logging
import argparse
import sys

_log = logging.getLogger('some')


class DataError(Exception):
    pass


def _process(arguments, others):
    """
    Process data specified in ``arguments`` (the --something arguments from
    the command line)and ``others``. If the data can not be processed, raise
    `DataError`.
    """
    assert arguments is not None
    assert others is not None
    assert len(others) >= 1

    # Here we would normally process something.
    pass


def main(arguments=None):
    if arguments is None:
        arguments = sys.argv

    # Exit code: 0=success, >0=error.
    exit_code = 1

    # Process arguments. In case of errors, report them and exit.
    parser = argparse.ArgumentParser(usage='process some report')
    parser.add_argument("-o", "--out", dest="target_path",
        help="write report to FILE", metavar="FILE")
    arguments, others = parser.parse_args(arguments)
    if len(others) < 1:
        # Note: parser.error() raises SystemExit.
        parser.error('input files must be specified')

    try:
        _process(arguments, others)
        exit_code = 0  # Success!
    except KeyboardInterrupt:
        _log.error('stopped as requested by user')
    except (DataError, OSError) as error:
        _log.error(error)
    except Exception as error:
        _log.exception(error)
    return exit_code


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
