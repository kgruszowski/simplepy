import ply.lex as lex

tokens = [
    'NAME',
    'INT', 'FLOAT', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN',
    'GT', 'GTE', 'LT', 'LTE', 'EQ', 'NEQ', 'TRUE', 'FALSE',
    'COLON', 'COMMA',
    'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'LSQBRACK', 'RSQBRACK',
    'INDENT', 'NEWLINE'
]

reserved = {
    'print': 'PRINT',
    'def': 'DEF',
    'return': 'RETURN',

    'if': 'IF',
    'else': 'ELSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    'for': 'FOR',
    'in': 'IN',
    'while': 'WHILE'
}

tokens = tokens + list(reserved.values())

t_ignore = " \t"
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = '%'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = '{'
t_RBRACK = '}'
t_LSQBRACK = r'\['
t_RSQBRACK = r'\]'
t_GT = r'\>'
t_GTE = r'\>='
t_LT = r'\<'
t_LTE = r'\<='
t_EQ = r'\=='
t_NEQ = r'\!='
t_COLON = r'\:'
t_COMMA = r'\,'
t_INDENT = r'\|'
t_NEWLINE = r'\n'

def t_TRUE(t):
    'True'
    t.value = True
    return t


def t_FALSE(t):
    'False'
    t.value = False
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words
    return t


def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\'(?:\\"|.)*?\''
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t


def t_error(t):
    print("Illegal character '%s' at line '%d'" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


lexer = lex.lex()
# input = '''
# a = [1, 5, 10, 50]\n
# b = {name: 'Kamil', age: 15}
# '''
# lexer.input(input)
# for token in lexer:
#     print('line %d: %s(%s)' %(token.lineno, token.type, token.value))