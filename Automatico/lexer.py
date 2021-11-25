import ply.lex as lex

# To handle reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'char': 'CHAR',
    'float': 'FLOAT',
    'void': 'VOID',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'bool': 'BOOL',
    '!': 'NOT',
    'break': 'BREAK',
    'for': 'FOR',
    'in' : 'IN',
    'do': 'DO'
}

# List of token names.   This is always required
tokens = [
    'INTNUMBER',
    'FLOATNUMBER',
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'AND',
    'OR',
    'GREATER',
    'GREATERTHAN',
    'LOWER',
    'LOWERTHAN',
    'SEMMICOLON',
    'ASSIGMENT',
    'EQUALS',
    'BLOCKCOMMENT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'COMMA'
] + list(reserved.values())

# Regular expression rules for simple tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_BLOCKCOMMENT = r'\/\*(\*(?!\/)|[^*])*\*\/'
t_DIVIDE = r'/'
t_MOD = r'%'
t_GREATERTHAN = r'\b>=\b'
t_GREATER = r'\>'
t_LOWERTHAN = r'\b<=\b'
t_LOWER = r'\<'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMMICOLON = r'\;'
t_COMMA = r'\,'
t_AND = r'\band\b'
t_OR = r'\bor\b'
t_EQUALS = r'\b==\b'
t_ASSIGMENT = r'\='


# A regular expression rule with some action code

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')    # Check for reserved words
    return t


def t_FLOATNUMBER(t):
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    return t


def t_INTNUMBER(t):
    r'[-+]?[0-9]+'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


    # Build the lexer
lexer = lex.lex()

# Test it out
data = '''
int a = 5 + 6.679, b = 0;
if (a==11)
bool fg = false
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
