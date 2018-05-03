import ast

ast.NameConstant

tree = ast.parse('''
False
''')
print(ast.dump(tree, annotate_fields=False))
