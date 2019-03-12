"""
Simple example for logging with Python.
"""
import logging

_log = logging.getLogger('example')  # use '__name__' for module name


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    _log.info('hello world!')

    _log.debug('located at: %s', __file__)
