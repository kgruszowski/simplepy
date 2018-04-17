import ply.yacc as yacc
from lexer import *



# arith_expr: term (('+'|'-') term)*
def p_artih_expr(p):
    '''arith_term : term PLUS term
                | term MINUS term
                | term
    '''
    pass

# term: factor (('*'|'@'|'/'|'%'|'//') factor)*
def p_term(p):
    '''term : factor TIMES factor
            | factor DIVIDE factor
            | factor MOD factor
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
    '''
    atom_expr : atom
    '''
    pass


# atom: ('(' [yield_expr|testlist_comp] ')' |
#        '[' [testlist_comp] ']' |
#        '{' [dictorsetmaker] '}' |
#        NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
def p_atom(p):
    '''
    atom : NAME
        | number
        | STRING
        | TRUE
        | FALSE
    '''
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


yacc.yacc()

s = '+5'
yacc.parse(s)