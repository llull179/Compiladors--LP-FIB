if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor
class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0
    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'MES(+)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1
    def visitMultiplicacio(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'MULT(*)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1
    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        print('   '*  self.nivell + 'REST(-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1
    def visitDivisio(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'Div(/)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1
        
    def visitPotencia(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'Pow(**)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')