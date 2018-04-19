import ply.yacc as yacc
from lexer import *


def p_stmt(p):
    '''stmt : simple_stmt
            | compound_stmt
    '''
    pass


def p_compound_stmt(p):
    '''compound_stmt : if_stmt NEWLINE'''


def p_simple_stmt(p):
    '''simple_stmt : small_stmt NEWLINE
    '''
    pass


def p_small_stmt(p):
    '''small_stmt : test
                | flow_stmt
    '''
    pass



def p_flow_stmt(p):
    '''flow_stmt : RETURN
                | BREAK
                | CONTINUE
    '''
    pass

# def p_compound_stmt(p):

def p_if_stmt(p):
    '''if_stmt : IF test COLON suite'''
    pass


def p_suite(p):
    '''suite : simple_stmt
            | LBRACK NEWLINE stmt RBRACK
    '''
    pass


# or_test: and_test ('or' and_test)*
# and_test: not_test ('and' not_test)*
def p_test(p):
    '''test : OR not_test
            | AND not_test
            | not_test
    '''
    pass


# 'not' not_test | comparison
def p_not_test(p):
    '''not_test : NOT not_test
                | comparison'''
    pass


# comparison: expr(comp_op expr) *
def p_comparison(p):
    '''comparison : expr comp_op expr
                | expr
    '''
    pass


# comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
def p_comp_op(p):
    '''comp_op : GT
            | GTE
            | LT
            | LTE
            | EQ
            | NEQ
    '''


# arith_expr: term (('+'|'-') term)*
# term: factor (('*'|'@'|'/'|'%'|'//') factor)*
def p_expr(p):
    '''expr : factor PLUS factor
            | factor MINUS factor
            | factor TIMES factor
            | factor DIVIDE factor
            | factor
    '''
    pass


# factor: ('+'|'-'|'~') factor | power
def p_factor(p):
    '''factor : PLUS factor
            | MINUS factor
            | atom_expr'''
    pass


# atom_expr: [AWAIT] atom trailer*
def p_atom_expr(p):
    '''atom_expr : atom'''
    pass


# atom: ('(' [yield_expr|testlist_comp] ')' |
#        '[' [testlist_comp] ']' |
#        '{' [dictorsetmaker] '}' |
#        NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
def p_atom(p):
    '''atom : LPAREN list_expr RPAREN
            | LSQBRACK list_expr RSQBRACK
            | LBRACK dict_expr RBRACK
            | NAME
            | number
            | STRING
            | TRUE
            | FALSE
    '''
    pass


# testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
def p_list_expr(p):
    '''list_expr : atom_expr COMMA list_expr
                | atom_expr
    '''
    pass


# dictorsetmaker: ( ((test ':' test | '**' expr)
#                   (comp_for | (',' (test ':' test | '**' expr))* [','])) |
#                  ((test | star_expr)
#                   (comp_for | (',' (test | star_expr))* [','])) )
def p_dict_expr(p):
    '''dict_expr : NAME COLON atom_expr COMMA dict_expr
                | NAME COLON atom_expr'''
    pass


def p_number(p):
    '''number : INT
            | FLOAT
    '''
    pass


def p_error(p):
    if p:
        print("Syntax error at {} in line {}, type {}".format(p.value, p.lineno, p.type))
    else:
        print("Syntax error at EOF")

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

parser = yacc.yacc()

s = '''if a < c: {
if d > 10: {
'asd'
}
}
'''
result = parser.parse(s, debug=log)