import ply.lex as lex

tokens = [
    'PLUS',
    'STAR',
    'EPSILON',
    'LETTER',
    'LPAREN',
    'RPAREN',
    'SEMI'
] 


t_PLUS = r'\+'
t_STAR = r'\*'
t_EPSILON = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r'\;'


def t_LETTER(t):
    r'[a-zA-Z0-9]'
    t.value = str(t.value)
    return t


# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    raise Exception('LEXER ERROR')


lex.lex()