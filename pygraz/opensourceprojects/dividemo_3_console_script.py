"""
dividemo - tool to divide two integer numbers.
"""
import argparse
import logging
import sys


def divided(divident, divisor):
    return divident // divisor  # //=integer division


def main(arguments):
    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='divide two integer numbers.')
    parser.add_argument('divident', metavar='DIVIDENT', type=int,
                        help='number to divide')
    parser.add_argument('divisor', metavar='DIVISOR', type=int,
                        help='number to divide by')
    args = parser.parse_args(arguments)
    if args.divisor == 0:
        parser.error('DIVISOR must not be 0')

    # Process arguments and print result.
    result = divided(args.divident, args.divisor)
    print(result)


def run():
    logging.basicConfig(level=logging.INFO)
    main(sys.argv[1:])


if __name__ == '__main__':
    run()
