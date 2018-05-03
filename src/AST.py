class Node(object):
    pass


class Module(Node):
    def __init__(self, body):
        self.type = 'module'
        self.body = body


class StatementList(Node):
    def __init__(self):
        self.statement_list = []

    def add_statement(self, statement_list):
        self.statement_list.append(statement_list)


class While(Node):
    def __init__(self, test, body, orelse):
        self.type = 'while'
        self.test = test
        self.body = body
        self.orelse = orelse


class If(Node):
    def __init__(self, test, body, orelse):
        self.type = 'if'
        self.test = test
        self.body = body
        self.orelse = orelse


class BoolOp(Node):
    def __init__(self, op, left, right):
        self.type = 'boolop'
        self.op = op
        self.left = left
        self.right = right

class Compare(Node):
    def __init__(self, left, op, right):
        self.type = 'compare'
        self.left = left
        self.right = right
        self.op = op


class Assign(Node):
    def __init__(self, id, expression):
        self.type = 'assign'
        self.id = id
        self.expression = expression


class BinOp(Node):
    def __init__(self, left, op, right):
        self.type = 'binop'
        self.left = left
        self.right = right
        self.op = op


class Number(Node):
    def __init__(self, value):
        self.type = 'number'
        self.value = value
