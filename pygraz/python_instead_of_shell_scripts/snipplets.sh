#!/usr/bin/env sh
# Shell script snipplets.

# Print a message
name='Alice'
echo Hello $name

# Find lines with word 'er'.
grep "\ber\b" glocke.txt

# Find files matching a pattern
find /Users/roskakori/workspace/talks -name "*.py"

# Count number of lines in glocke.txt.
wc -l glocke.txt

wc -l no_such_file.txt
if [[ $? -ne 0 ]]; then
    echo cannot count lines in no_such_file.txt
fi
