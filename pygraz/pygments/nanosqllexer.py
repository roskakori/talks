"""
Simple demo lexer for a small subset of SQL.
"""
from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, Number, String, \
    Operator, Punctuation, Whitespace


_NANOSQL_KEYWORDS = (
    'as',
    'from',
    'select',
    'where',
)


class NanoSqlLexer(RegexLexer):
    name = 'NanoSQL'
    aliases = ['nanosql']
    filenames = ['*.nsql']

    tokens = {
        'root': [
            # TODO: Add rules.
        ],
    }
