# -*- coding: utf-8 -*-
"""
Examples and code excerpts for talk on "Unicode survival kit".
"""
english_text = 'cheese spaetzle: 10 euro'
print(english_text)
german_text = 'Käsespätzle: 10€'
german_text = u'Käsespätzle: 10€'
german_text = 'K\u00e4sesp\u00e4tzle: 10\u20ac'
print(german_text)
data = b'spae\x74\x7ale'
print(data)

_ENGLISCH_PANGRAM = 'the quick brown fox jumps over the lazy white dog'
_GERMAN_PANGRAM = 'Falsches Üben von Xylophonmusik quält jeden größeren Zwerg'
_GERMAN_EURO_PANGRAM = 'Add'

def hexdump_lines(text_bytes, break_after=16):
    hex_part = ''
    text_part = ''

    line_address = 0
    for address, code in enumerate(text_bytes):
        hex_part += '%02x ' % code
        if (code >= 0x20) and (code <= 0x7f):
            text_part += chr(code)
        else:
            text_part += '.'
        if address % break_after == break_after - 1:
            yield line_address, hex_part, text_part
            line_address = address
            hex_part = ''
            text_part = ''
    if hex_part != '':
        yield line_address, hex_part, text_part

def print_hexdump(text_bytes):
    BREAK_AFTER = 16
    for address, hex_part, text_part in hexdump_lines(text_bytes, BREAK_AFTER):
        print('%08x: %-*s  |%s|' % (address, 3 * BREAK_AFTER, hex_part, text_part))

for encoding in ('utf-32', 'utf-8', 'cp1252'):
    encoded_bytes = 'Spätzle: €10'.encode(encoding)
    print('%-6s: %s' % (encoding, encoded_bytes))
    print_hexdump(encoded_bytes)

for encoding in ('utf-8', 'cp1252'):
    print(encoding)
    print_hexdump(_GERMAN_EURO_PANGRAM.encode(encoding))

# Code works in Python 2.6+ and 3.2+.
import io
with io.open('menu.txt', 'w', encoding='utf-32') as menu_file:
    menu_file.write(u'Spätzle: 10€')

with io.open('menu.txt', 'w', encoding='utf-16') as menu_file:
    menu_file.write(u'Spätzle: 10€')

# print('Spätzle: 10€'.encode('utf-8'))
for c in ['ü', '€']:
    for encoding in ['utf-8', 'cp1252', 'iso-8859-15']:
        print('%s %s --> %r' % (c, encoding, c.encode(encoding)))

#import sys
#print(sys.getdefaultencoding())
