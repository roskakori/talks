"""
Command line utility to copy files.
"""
import argparse
import logging
import sys


_log = logging.getLogger('copytool')


def copy(source, target, preserve='all', is_recursive=False):
    _log.info('copy %s to %s', source, target)
    # TODO: Actuall copy files using shutil.


def main(args=None):
    if args is None:
        args = sys.argv

    # Process arguments. In case of error, report it and exit.
    parser = argparse.ArgumentParser(description='copy files or folders')
    parser.add_argument(
        'sources', metavar='SOURCE', nargs='+',
        help="file or folder to copy")
    parser.add_argument(
        'target', metavar='TARGET',
        help="target file or folder")
    parser.add_argument(
        '--recursive', '-r', action='store_true',
        help='recursively copy folders')
    parser.add_argument(
        '--preserve', '-p',
        choices=['access', 'all', 'time', 'none'],
        default='all',
        help='preserve specified attributes, default: %(default)s')
    parser.add_argument(
         '--version', action='version', version='%(prog)s 1.0')
    arguments = parser.parse_args(args)

    # Exit code: 0=success, >0=error.
    exit_code = 1
    try:
        for source in arguments.sources:
            copy(
                source, arguments.target,
                is_recursive=arguments.recursive,
                preserve=arguments.preserve)
        exit_code = 0  # Success!
    except KeyboardInterrupt:
        _log.error('stopped as requested by user')
    except (OSError) as error:
        _log.error(error)
    except Exception as error:
        _log.exception(error)
    return exit_code


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
