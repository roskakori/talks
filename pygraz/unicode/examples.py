# -*- coding: utf-8 -*-
"""
Examples and code excerpts for talk on "Erste Hilfekasten für Unicode mit Python".
"""
english_text = 'cheese spaetzle: 10 euro'
print(english_text)
german_text = 'Käsespätzle: 10€'
german_text = u'Käsespätzle: 10€'
german_text = 'K\u00e4sesp\u00e4tzle: 10\u20ac'
print(german_text)

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

# Code works in Python 2.6+ and 3.3+.
import io
with io.open('menu.txt', 'w', encoding='utf-32') as menu_file:
    menu_file.write(u'Spätzle: 10€')

with io.open('menu.txt', 'w', encoding='utf-16') as menu_file:
    menu_file.write(u'Spätzle: 10€')

# print('Spätzle: 10€'.encode('utf-8'))
for c in ['ü', '€']:
    for encoding in ['utf-8', 'cp1252', 'iso-8859-15']:
        print('%s %s --> %r' % (c, encoding, c.encode(encoding)))

# Show the (basically random) default encoding.
import sys
print(sys.getdefaultencoding())

# The euro sign in its various incarnations.
euro_sign = '€'
euro_sign = '\u20ac'
euro_sign = chr(0x20ac)  # Python 2: unichr(0x20a0)
euro_sign = chr(2 * 16**3 + 0 * 16**2 + 10 * 16**1 + 12 * 16**0)
euro_sign = chr(8364)
euro_sign = '\N{EURO SIGN}'
import unicodedata
euro_sign = unicodedata.lookup('EURO SIGN')
print(euro_sign)

print(hex(ord('樹')))
print('\u20ac'.encode('utf-8'))  # euro sign as UTF-8
_= b'\xe2\x82\xac'

# Example stack traces for UnicodeError.
import sys
import traceback
try:
    'Spätzle: 10€'.encode('ascii')
except UnicodeEncodeError as error:
    traceback.print_exc(file=sys.stdout)

try:
    spaetzle_bytes = 'Spätzle: 10€'.encode('cp1252')
    print(spaetzle_bytes)
    spaetzle_bytes.decode('utf-8')
except UnicodeDecodeError as error:
    traceback.print_exc(file=sys.stdout)

# Hack cp1252 to map every byte, even undefined ones like b'\x81'.
import codecs
from encodings import cp1252

decoding_table = ''.join([
    code if code != '\ufffe' else chr(index) \
    for index, code in enumerate(cp1252.decoding_table)
])
assert '\ufffe' not in decoding_table
cp1252.decoding_table = decoding_table
cp1252.encoding_table = codecs.charmap_build(decoding_table)

# Führt normalerweise zu UnicodeEncodeError.
print('\x81'.encode('cp1252'))

# Normalisation.
import unicodedata
print('\u0049')
print('\u2160')
print_hexdump([code for code in unicodedata.normalize('NFC', 'ä').encode('utf-16be')])
print_hexdump([code for code in unicodedata.normalize('NFD', 'ä').encode('utf-16be')])

with io.open('\u0049.tmp', 'wb'):
    pass
with io.open('\u2160.tmp', 'wb'):
    pass
