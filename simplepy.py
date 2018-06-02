from simplepy.lexer import Lexer
from simplepy.parser import Parser
from simplepy.interpreter import Interpreter
from simplepy.tree_printer import TreePrinter
import ply.yacc as yacc
import logging
import sys


logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

if len(sys.argv) == 1:
    print("Usage: python3 %s filename" % __file__)
else:
    with open('example/{}'.format(sys.argv[1]), 'r') as content_file:
        file_input = content_file.read()

    lexer = Lexer()
    parser = yacc.yacc(module=Parser)
    ast = parser.parse(file_input, debug=log, lexer=lexer)

    ast.accept(Interpreter())

    # print(program)
