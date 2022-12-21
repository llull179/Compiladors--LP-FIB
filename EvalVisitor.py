if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor
from collections import defaultdict


class representacioFuncio():
    def __init__(self, nom, params, context):
        self.nom = nom
        self.params = params
        self.context = context


class EvalVisitor(FunxVisitor):

    def __init__(self):
        self.dictFuncions = {}
        self.pilaContexte = [{}]

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print("Out: "+ str(self.visit(l[0])))

    '''
    --------------------------------------------------------
    -------------------OPERACIONS BÀSIQUES------------------
    --------------------------------------------------------
    '''

    def visitBrackets(self, ctx: FunxParser.BracketsContext):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitBracketsComp(self, ctx: FunxParser.BracketsCompContext):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])

    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    def visitMultiplicacio(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    def visitPotencia(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) ** self.visit(l[2])

    def visitDivisio(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[2]) == 0:
            raise Exception("ERR: divisio per 0")
        else:
            return self.visit(l[0]) / self.visit(l[2])

    '''
    --------------------------------------------------------
    -------------------OPERACIONS BOOLEANES------------------
    --------------------------------------------------------
    '''

    def visitMaj(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) > self.visit(l[2]))

    def visitMajeq(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) >= self.visit(l[2]))
        

    def visitMen(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) < self.visit(l[2]))

    def visitMeneq(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) <= self.visit(l[2]))

    def visitEq(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) == self.visit(l[2]))

    def visitDif(self, ctx: FunxParser.MajContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) != self.visit(l[2]))

    '''
    --------------------------------------------------------
    -------------------OPERACIONS LÒGIQUES------------------
    --------------------------------------------------------
    '''

    def visitAnd(self, ctx: FunxParser.AndContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) and self.visit(l[2]))


    def visitOr(self, ctx: FunxParser.OrContext):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) or self.visit(l[2]))

    def visitXor(self, ctx: FunxParser.XorContext):
        l = list(ctx.getChildren())
        if not self.visit(l[0]) and self.visit(l[2]):
            return 1
        elif self.visit(l[0]) and not self.visit(l[2]):
            return 1
        else:
            return 0

    def visitNot(self, ctx: FunxParser.NotContext):
        l = list(ctx.getChildren())
        return not self.visit(l[1])

    '''
    --------------------------------------------------------
    -------------------ASSIGNACIO VARIABLES-----------------
    --------------------------------------------------------
    '''

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        # self.taulaSimbols[l[0].getText()] = self.visit(l[2])
        self.pilaContexte[-1][l[0].getText()] = self.visit(l[2])

    '''
    --------------------------------------------------------
    -------------------VISITA VALORS-----------------
    --------------------------------------------------------
    '''

    def visitValorInt(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitValorFloat(self, ctx):
        l = list(ctx.getChildren())
        return float(l[0].getText())

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getText() in self.pilaContexte[-1]:
            return self.pilaContexte[-1][l[0].getText()]
        else:
            return 0

    def visitCjtExpr(self, ctx: FunxParser.CjtExprContext):
        l = list(ctx.getChildren())
        val = []
        for p in l:
            val.append(self.visit(p))
        return val

    def visitCjtParams(self, ctx: FunxParser.CjtParamsContext):
        l = list(ctx.getChildren())
        par = []
        for p in l:
            par.append(p.getText())
        return par
    '''
    --------------------------------------------------------
    -------------------CONDICIONALS------------------
    --------------------------------------------------------
    '''

    def visitIfThen(self, ctx):
        l = list(ctx.getChildren())
        comparacio = self.visit(l[1])
        result = None
        if comparacio:
            i = 3
            while l[i].getText() != '}' and result is None:
                result = self.visit(l[i])
                i = i + 1
        return result

    def visitIfThenElse(self, ctx: FunxParser.IfThenElseContext):
        l = list(ctx.getChildren())
        comparacio = self.visit(l[1])
        result = None
        if comparacio:
            i = 3
            while l[i].getText() != '}' and result is None:
                result = self.visit(l[i])
                i = i + 1
        else:
            i = 5
            while l[i].getText() != '}' and result is None:
                result = self.visit(l[i])
                i = i + 1
        return result

    '''
    --------------------------------------------------------
    -------------------BUCLES------------------
    --------------------------------------------------------
    '''
    
    def visitBucleWhile(self, ctx: FunxParser.BucleWhileContext):
        l = list(ctx.getChildren())
        result = None
        while self.visit(l[1]):
            i = 3
            while l[i].getText() != "}" and result is None:
                result = self.visit(l[i])
                i = i + 1
        return result
    
    def visitBucleFor(self, ctx: FunxParser.BucleForContext):
        l = list(ctx.getChildren())
        result = None
        self.visit(l[1])
        while self.visit(l[3]):
            i = 7
            while l[i].getText() != '}' and result == None:
                result = self.visit(l[i])
                i = i + 1
            self.visit(l[5])
        return result

    '''
    --------------------------------------------------------
    -------------------FUNCIONS------------------
    --------------------------------------------------------
    '''

    def visitDefinicioFuncio(self, ctx: FunxParser.DefinicioFuncioContext):
        l = list(ctx.getChildren())
        idFun = l[0].getText()
        if (idFun in self.dictFuncions):
            raise Exception("ERR: La funcio " + idFun + " ja esta definida")

        ''' codiFun = []
        i = 3
        for i in range(i, len(l)-1):
            codiFun.append(l[i])
        '''
        self.dictFuncions[idFun] = representacioFuncio(
            idFun, self.visit(l[1]), ctx)

    def visitFuncioCall(self, ctx: FunxParser.FuncioCallContext):
        l = list(ctx.getChildren())
        idFun = l[0].getText()
        if (idFun not in self.dictFuncions):
            raise Exception("ERR: La funcio " + idFun + " no existeix")

        parFun = self.dictFuncions[idFun].params
        valFun = self.visit(l[1])

        if len(parFun) != len(valFun):
            raise Exception("ERR: Els parametres no coincideixen")

        ctxActual = {}

        i = 0
        while i < len(valFun):
            ctxActual[parFun[i]] = valFun[i]
            i = i + 1

        self.pilaContexte.append(ctxActual)
        result = None
        i = 0

        con = list(self.dictFuncions[idFun].context.getChildren())
        while con[i].getText() != "{":
            i += 1
        i += 1
        while con[i].getText() != "}" and result is None:
            result = self.visit(con[i])
            i = i + 1

        self.pilaContexte.pop()
        return result
