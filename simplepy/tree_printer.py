import simplepy.ast as AST

LEVEL_TOKEN = "| "


def addToClass(classname):

    def decorator(fun):
        setattr(classname, fun.__name__, fun)
        return fun
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, level=0):
        raise Exception("printTree not defined in class" + self.__class__.__name__)

    @addToClass(AST.Str)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret = ret + str(self.value)
        return ret

    @addToClass(AST.Number)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret = ret + str(self.value)
        return ret

    @addToClass(AST.Const)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret = ret + str(self.value)
        return ret

    @addToClass(AST.Str)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret = ret + str(self.value)
        return ret

    @addToClass(AST.Name)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret = ret + str(self.id)
        return ret

    @addToClass(AST.ExprList)
    def printTree(self, level=0):
        ret = ""
        x = ""
        for item in self.expression_list:
            ret += x + item.printTree(level)
            x = "\n"
        return ret

    @addToClass(AST.Tuple)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret += "TUPLE\n" + self.values.printTree(level + 1)

        return ret

    @addToClass(AST.List)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level
        ret += "LIST\n" + self.values.printTree(level + 1)

        return ret

    @addToClass(AST.BinOp)
    def printTree(self, level=0):
        return LEVEL_TOKEN * level + self.op + "\n" + self.left.printTree(level+1) + "\n" + self.right.printTree(level+1)

    @addToClass(AST.Assign)
    def printTree(self, level=0):
        return LEVEL_TOKEN * level + "=\n" + LEVEL_TOKEN * (level+1) + str(self.id) + "\n" + self.expression.printTree(level + 1)

    @addToClass(AST.Compare)
    def printTree(self, level=0):
        return LEVEL_TOKEN * level + self.op + "\n" + self.left.printTree(level + 1) + "\n" + self.right.printTree(
            level + 1)

    @addToClass(AST.BoolOp)
    def printTree(self, level=0):
        return LEVEL_TOKEN * level + self.op + "\n" + self.left.printTree(level + 1) + "\n" + self.right.printTree(
            level + 1)

    @addToClass(AST.If)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level

        if not self.orelse:
            ret += "IF\n" + self.test.printTree(level + 1) + "\n" + self.body.printTree(level + 1)
        else:
            ret += "IF\n" + self.test.printTree(level + 1) + "\n" + self.body.printTree(level + 1) + "\n" + self.orelse.printTree(level + 1)

        return ret

    @addToClass(AST.While)
    def printTree(self, level=0):
        ret = LEVEL_TOKEN * level

        if not self.orelse:
            ret += "WHILE\n" + self.test.printTree(level + 1) + "\n" + self.body.printTree(level + 1)
        else:
            ret += "WHILE\n" + self.test.printTree(level + 1) + "\n" + self.body.printTree(
                level + 1) + "\n" + self.orelse.printTree(level + 1)

        return ret

    @addToClass(AST.Print)
    def printTree(self, level=0):
        return LEVEL_TOKEN * level + 'PRINT \n' + self.value.printTree(level + 1)

    @addToClass(AST.StatementList)
    def printTree(self, level=0):
        ret = ""
        x = ""
        for item in self.statement_list:
            ret += x + item.printTree(level)
            x = "\n"
        return ret

    @addToClass(AST.Module)
    def printTree(self, level=0):
        return self.body.printTree()