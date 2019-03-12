"""
Example for logging and error with stack trace.
"""
import logging

_log = logging.getLogger('example')


def process_data(data_path: str):
    with open(data_path, encoding='utf-8') as data_file:
        for line in data_file:
            # Here we would actually process data
            pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    important_data_path = 'no_such_data.txt'
    try:
        process_data(important_data_path)
    except OSError as error:
        _log.error('cannot process data file "%s": %s',
                   important_data_path, error, exc_info=True)
