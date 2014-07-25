"""
Example for chaining an `Exception` to another as cause.
"""


def process_something(line):
    pass


def process_data_file_possibly_raising_chained_error(dataFile):
    assert dataFile is not None

    lineNumber = 1
    try:
        # Process all heights read from `dataFile`.
        for lineNumber, line in enumerate(dataFile, start=1):
            process_something(int(line))
    except ValueError as error:
        raise ValueError('%s (%d): cannot process something' % (
            dataFile.name, lineNumber)) \
            from error  # <-- Chained error.


if __name__ == '__main__':
    with open('some.txt', 'rb') as dataFile:
        process_data_file_possibly_raising_chained_error
