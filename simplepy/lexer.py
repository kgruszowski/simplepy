import ply.lex as lex


class Lexer(object):

    def __init__(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()

    tokens = [
        'NAME',
        'INT', 'FLOAT', 'STRING',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN',
        'GT', 'GTE', 'LT', 'LTE', 'EQ', 'NEQ', 'TRUE', 'FALSE', 'NONE',
        'COLON', 'SEMICOLON', 'COMMA',
        'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'LSQBRACK', 'RSQBRACK',
    ]

    reserved = {
        'print': 'PRINT',
        'return': 'RETURN',
        'break': 'BREAK',
        'continue': 'CONTINUE',

        'if': 'IF',
        'else': 'ELSE',
        'and': 'AND',
        'or': 'OR',

        'while': 'WHILE'
    }

    tokens = tokens + list(reserved.values())

    t_ignore = " \t"
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MOD = r'%'
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
    t_SEMICOLON = r'\;'
    t_COMMA = r'\,'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_TRUE(self, t):
        'True'
        t.value = True
        return t

    def t_FALSE(self, t):
        'False'
        t.value = False
        return t

    def t_NONE(self, t):
        'None'
        t.value = None
        return t

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = Lexer.reserved.get(t.value, 'NAME')  # Check for reserved words
        return t

    def t_FLOAT(self, t):
        r'\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r'\'(?:\\"|.)*?\''
        t.value = bytes(t.value.lstrip("'").rstrip("'"), "utf-8").decode("unicode_escape")
        return t

    def t_error(self, t):
        print("Illegal character '%s' at line '%d'" % (t.value[0], t.lexer.lineno))
        t.lexer.skip(1)