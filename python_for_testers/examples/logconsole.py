import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('myapp')
log.info('Hello world')

name = 'Alice'
size = 172
log.info('%s is %dcm tall', name, size)
