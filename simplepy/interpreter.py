from simplepy.visit import *
import simplepy.ast as AST


class Interpreter(object):

    def __init__(self):
        self.variables = {}

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Module)
    def visit(self, node):
        node.body.accept(self)

    @when(AST.StatementList)
    def visit(self, node):
        result = []
        for statement in node.statement_list:
            result.append(statement.accept(self))
        return result

    @when(AST.Print)
    def visit(self, node):
        print(node.value.accept(self))

    @when(AST.While)
    def visit(self, node):
        if node.test.accept(self):
            while node.test.accept(self):
                node.body.accept(self)
        else:
            if node.orelse != []:
                return node.orelse.accept(self)
            else:
                pass

    @when(AST.If)
    def visit(self, node):
        if node.test.accept(self):
            return node.body.accept(self)
        else:
            if node.orelse != []:
                return node.orelse.accept(self)
            else:
                pass

    @when(AST.BoolOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return bool(eval("a " + node.op + " b", {"a": r1, "b": r2}))

    @when(AST.Compare)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return bool(eval("a" + node.op + "b", {"a": r1, "b": r2}))

    @when(AST.Assign)
    def visit(self, node):
        expr_accept = node.expression.accept(self)
        self.variables[node.id] = expr_accept
        return self.variables[node.id]

    @when(AST.BinOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        r1Str = str(r1)
        r2Str = str(r2)
        pos1 = r1Str.find('.')
        pos2 = r2Str.find('.')

        if pos1 != -1 or pos2 != -1:
            return float(eval("a" + node.op + "b", {"a": r1, "b": r2}))
        else:
            return int(eval("a" + node.op + "b", {"a": r1, "b": r2}))

    @when(AST.List)
    def visit(self, node):
        return list(node.values.accept(self))

    @when(AST.Tuple)
    def visit(self, node):
        return tuple(node.values.accept(self))

    @when(AST.ExprList)
    def visit(self, node):
        result = []
        for expr in node.expression_list:
            result.append(expr.accept(self))
        return result

    @when(AST.Name)
    def visit(self, node):
        return self.variables[node.id]

    @when(AST.Const)
    def visit(self, node):
        return node.value

    @when(AST.Number)
    def visit(self, node):
        numStr = str(node.value)
        pos = numStr.find('.')

        if pos != -1:
            return float(node.value)
        else:
            return int(node.value)

    @when(AST.Str)
    def visit(self, node):
        return node.value
