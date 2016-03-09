# Simple example application reading a config.
import configparser
import logging
import logging.config
import logging.handlers
import os.path

log = logging.getLogger('myapp')


class MyApp(object):
    def __init__(self, config_path):
        # Setup config with defaults.
        config = configparser.ConfigParser()
        config['myapp'] = {}
        config['myapp']['fullscreen'] = 'false'
        config['myapp']['timeout'] = '60'

        # Update config from file.
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config.read_file(config_file)

        self.connection = config.get('myapp', 'connection')
        self.is_fullscreen = config.getboolean('myapp', 'fullscreen')
        self.timeout = config.getint('myapp', 'timeout')

    def work(self):
        log.debug('connection=%s', self.connection)
        log.info('is_fullscreen=%s', self.is_fullscreen)
        log.info('timeout=%d', self.timeout)


if __name__ == '__main__':
    config_path = os.path.join('examples', 'myapp.cfg')
    logging.config.fileConfig(config_path)
    myapp = MyApp(config_path)
    myapp.work()
