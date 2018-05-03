import ast

ast.Module

tree = ast.parse('''
a = 10

if a > 15:
    a = 8 + a * 5
''')
print(ast.dump(tree, annotate_fields=False))
