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
            (words(_NANOSQL_KEYWORDS, suffix=r'\b'), Keyword),
            (r'\s+', Whitespace),
            (r'--.*?$', Comment),
            (r'\d+', Number),
            (r'\w+', Name),
            (r'[.,;:]', Punctuation),
            (r'[<>=/*+-]', Operator),
            ('\'', String, 'string'),
        ],
        'string': [
            ("''", String),
            (r'[^\']', String),
            ("'", String, '#pop')
        ]
    }
