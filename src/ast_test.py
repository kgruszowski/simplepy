import ast

ast.Tuple

tree = ast.parse('''
a = 10
b = 15
''')
print(ast.dump(tree, annotate_fields=False))
