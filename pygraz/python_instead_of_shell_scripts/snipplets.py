"""
Code snipplets to show how to do basic Python tasks similar to shell tasks.
"""

# Print a message
name = 'Alice'
print('Hello ' + name)


# Log a message
import logging

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger('demo')
_log.info('Hello %s', name)


# Traverse file line by line.
with open('glocke.txt', encoding='utf-8') as poem_file:
    for line in poem_file:
        line = line.rstrip('\n')  # Remove possible trailing linefeed.
        print(line)


# Regular expression to match word "er" (German for "he").
import re

er_regex = re.compile(r'\ber\b')
if er_regex.search('Was mach er da?'):
    print('found it!')

# Print all lines containing the word 'er'.
with open('glocke.txt', encoding='utf-8') as poem_file:
    for line in poem_file:
        if er_regex.search(line):
            print(line.rstrip('\n'))

# Collect lines containing the word 'er' in a list
# using list comprehension.
with open('glocke.txt', encoding='utf-8') as poem_file:
    lines_with_er = [
        line.rstrip('\n') for line in poem_file
        if er_regex.search(line)
    ]
print(lines_with_er)


# Find files matching pattern.
import glob

file_pattern = '/Users/roskakori/workspace/talks/**/*.py'
for path in glob.iglob(file_pattern, recursive=True):
    print(path)


# Platform independent path operations
import os

print(os.sep)  # The seperator between paths, e.g. '/' or '\'

# Combine path parts.
glocke_path = os.path.join(os.getcwd(), 'glocke.txt')
print(glocke_path)

# Extract folder, name and suffix
folder, name = os.path.split(glocke_path)
print(folder)
print(name)

base_name, suffix = os.path.splitext(name)
print(base_name)
print(suffix)


# Call an external program and process the output
import subprocess

wc_result = subprocess.check_output(
    ['wc', '-l', glocke_path],
    encoding='utf-8')

# Extract line count from string like '      23 .../glocke.txt'.
wc_result_words = wc_result.split()
first_wc_result_word = wc_result_words[0]
glocke_line_count = int(first_wc_result_word)

print(glocke_path, 'has', glocke_line_count, 'lines')

try:
    wc_result = subprocess.check_output(
        ['wc', '-l', 'no_such_file.txt'],
        encoding='utf-8')
except subprocess.CalledProcessError as error:
    print('cannot count lines:', error)

# Parse command line arguments
import argparse

parser = argparse.ArgumentParser(description='copy files')
parser.add_argument(
    '--verbose', '-V', action='store_true', help='log each copied file')
parser.add_argument(
    '--log', metavar='LEVEL', choices=['debug', 'info', 'error'], dest='log_level',
    default='info', help='set log level to LEVEL (default: %(default)s)')
parser.add_argument(
    '--buffer', '-b', metavar='SIZE', dest='buffer_size', type=int, default=16,
    help='buffer size in kilo byte (default: %(default)s)')
parser.add_argument('--version', action='version', version='1.0')
parser.add_argument('sources', metavar='SOURCE', nargs='+', help='files to copy')
parser.add_argument('target', metavar='TARGET', help='target file or folder')

args = parser.parse_args(['--buffer=64', 'glocke.txt', 'bell.txt'])
print(args.sources)
print(args.target)
print(args.buffer_size)

args = parser.parse_args(['--help'])
