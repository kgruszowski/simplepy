import sys
import ply.yacc as yacc
from lexer import *
import AST

precedence = (
    ('nonassoc', 'LT', 'GT', 'LTE', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_program(p):
    '''program : stmt_list'''
    p[0] = AST.Module(p[1])


def p_stmt_list(p):
    '''stmt_list : stmt stmt_list
                | stmt
    '''
    if len(p) == 3:
        p[0] = AST.StatementList()
        p[0].add_statement(p[2])
    else:
        p[0] = AST.StatementList()
        p[0].add_statement(p[1])


def p_stmt(p):
    '''stmt : simple_stmt
            | compound_stmt
            | NEWLINE
    '''
    p[0] = p[1]


def p_compound_stmt(p):
    '''compound_stmt : if_stmt
                    | while_stmt
                    | print
    '''
    p[0] = p[1]


def p_simple_stmt(p):
    '''simple_stmt : small_stmt NEWLINE
    '''
    p[0] = p[1]


def p_small_stmt(p):
    '''small_stmt : test
                | flow_stmt
    '''
    p[0] = p[1]


def p_print(p):
    '''print : PRINT LPAREN small_stmt RPAREN'''
    pass


def p_flow_stmt(p):
    '''flow_stmt : RETURN
                | BREAK
                | CONTINUE
    '''
    p[0] = p[1]


def p_while_stmt(p):
    '''while_stmt : WHILE test COLON suite
                | WHILE test COLON suite ELSE COLON suite
    '''
    if len(p) == 5:
        p[0] = AST.While(p[2], p[4], [])
    else:
        p[0] = AST.While(p[2], p[4], p[7])


def p_if_stmt(p):
    '''if_stmt : IF test COLON suite
                | IF test COLON suite ELSE COLON suite
    '''
    if len(p) == 5:
        p[0] = AST.If(p[2], p[4], [])
    else:
        p[0] = AST.If(p[2], p[4], p[7])


def p_suite(p):
    '''suite : simple_stmt
            | LBRACK NEWLINE stmt_list RBRACK
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[3]


# or_test: and_test ('or' and_test)*
# and_test: not_test ('and' not_test)*
def p_test(p):
    '''test : comparison OR test
            | comparison AND test
            | comparison
    '''
    if len(p) == 4:
        p[0] = AST.BoolOp(p[2], p[1], p[3])
    else:
        p[0] = p[1]


# comparison: expr(comp_op expr) *
def p_comparison(p):
    '''comparison : expr comp_op expr
                | expr
    '''
    if len(p) == 4:
        p[0] = AST.Compare(p[1], p[2], p[3])
    else:
        p[0] = p[1]


# comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
def p_comp_op(p):
    '''comp_op : GT
            | GTE
            | LT
            | LTE
            | EQ
            | NEQ
    '''
    p[0] = p[1]


def p_assign_expr(p):
    '''expr : NAME ASSIGN expr'''
    p[0] = AST.Assign(p[1], p[3])

# arith_expr: term (('+'|'-') term)*
# term: factor (('*'|'@'|'/'|'%'|'//') factor)*
def p_expr(p):
    '''expr : factor PLUS expr
            | factor MINUS expr
            | factor TIMES expr
            | factor DIVIDE expr
            | factor MOD expr
            | factor
    '''
    if len(p) == 4:
        p[0] = AST.BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

# factor: ('+'|'-'|'~') factor | power
def p_factor(p):
    '''factor : PLUS factor
            | MINUS factor
            | atom_expr'''
    if len(p) == 2:
        p[0] = p[1]


# atom_expr: [AWAIT] atom trailer*
def p_atom_expr(p):
    '''atom_expr : atom'''
    p[0] = p[1]


# atom: ('(' [yield_expr|testlist_comp] ')' |
#        '[' [testlist_comp] ']' |
#        '{' [dictorsetmaker] '}' |
#        NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
def p_atom(p):
    '''atom : LPAREN list_expr RPAREN
            | LSQBRACK list_expr RSQBRACK
            | LBRACK dict_expr RBRACK
            | name
            | number
            | string
            | TRUE
            | FALSE
            | NONE
    '''
    if len(p) == 2:
        if isinstance(p[1], AST.Number) or isinstance(p[1], AST.Str) or isinstance(p[1], AST.Name):
            p[0] = p[1]
        else:
            p[0] = AST.Const(p[1])
    else:
        p[0] = p[1]


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


def p_name(p):
    '''name : NAME'''
    p[0] = AST.Name(p[1])


def p_number(p):
    '''number : INT
            | FLOAT
    '''
    p[0] = AST.Number(p[1])


def p_string(p):
    '''string : STRING'''
    p[0] = AST.Str(p[1])


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


if len(sys.argv) == 1:
    print("Usage: python3 %s filename" % __file__)
else:
    with open('../example/{}'.format(sys.argv[1]), 'r') as content_file:
        file_input = content_file.read()

    result = parser.parse(file_input, debug=log)
    print(result)