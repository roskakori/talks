import logging

# Create a logger and make it available throughout the module.
_log = logging.getLogger('some')


def processData(dataPath):
    _log.info(u'read "%s"', dataPath)
    with open(dataPath, 'rb') as dataFile:
        # Here we would actually process the data.
        pass


if __name__ == '__main__':
    # Set up logging to stderr.
    logging.basicConfig(level=logging.INFO)
    processData('data.txt')
