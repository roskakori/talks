"""
Toy application to exercise pygments.
"""
import os

import pygments.lexers
import pygments.token


_MODULE_FOLDER = os.path.dirname(__file__)
_EXAMPLE_SQL_PATH = os.path.join(_MODULE_FOLDER, 'example.sql')
_TRANSACT_SQL_PATH = os.path.join(_MODULE_FOLDER, 'transact.sql')


def print_tokens(source_path):
    # Read source code into string.
    with open(source_path, encoding='utf-8') as source_file:
        source_text = source_file.read()

    # Find a fitting lexer.
    lexer = pygments.lexers.guess_lexer_for_filename(
        source_path, source_text)

    # Print tokens from source code.
    for items in lexer.get_tokens(source_text):
        print(items)


_UPPER_EXAMPLE_SQL_PATH = os.path.join(_MODULE_FOLDER, 'example_upper.sql')
_LOWIFIED_EXAMPLE_SQL_PATH = os.path.join(_MODULE_FOLDER, 'example_lower.sql')


def lowify_sql_keywords(source_path, target_path):
    # Read source code into string.
    with open(source_path, encoding='utf-8') as source_file:
        source_text = source_file.read()

    # Find a fitting lexer.
    lexer = pygments.lexers.guess_lexer_for_filename(
        source_path, source_text)

    # Lex the source, convert keywords and write target file.
    with open(target_path, 'w', encoding='utf-8') as target_file:
        for token_type, token_text in lexer.get_tokens(source_text):
            # Check for keywords and convert them to lower case.
            if token_type == pygments.token.Keyword:
                token_text = token_text.lower()
            target_file.write(token_text)


if __name__ == '__main__':
    # print_tokens(_EXAMPLE_SQL_PATH)
    lowify_sql_keywords(_UPPER_EXAMPLE_SQL_PATH, _LOWIFIED_EXAMPLE_SQL_PATH)