from simplepy.lexer import Lexer
from simplepy.parser import Parser
from simplepy.interpreter import Interpreter
from simplepy.tree_printer import TreePrinter
import ply.yacc as yacc
import sys

if len(sys.argv) == 1:
    print("Usage: python3 %s filename" % __file__)
else:
    with open('example/{}'.format(sys.argv[1]), 'r') as content_file:
        file_input = content_file.read()

    parser = yacc.yacc(module=Parser)
    ast = parser.parse(file_input, lexer=Lexer())
    print('===== AST =====\n')
    print(ast)
    print('\n===== PROGRAM EXECUTION =====\n')
    ast.accept(Interpreter())
