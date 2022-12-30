from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from flask import render_template,Flask, request


if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

#Representació interna de les funcions

class representacioFuncio():
    def __init__(self, nom, params, context):
        self.nom = nom
        self.params = params
        self.context = context

'''
    --------------------------------------------------------
    -------------------INTERPRET!!------------------
    --------------------------------------------------------
'''
class Funx(FunxVisitor):

    def __init__(self):
        self.dictFuncions = {}
        self.pilaContexte = [{}]

    def getFunctions(self):
        return self.dictFuncions
        
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        return("Out: " + str(self.visit(l[0])))

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
            return int(self.visit(l[0]) / self.visit(l[2]))

    def visitModul(self, ctx: FunxParser.ModulContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) % self.visit(l[2])

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

    def visitValorIntNeg(self, ctx: FunxParser.ValorIntNegContext):
        l = list(ctx.getChildren())
        return -1 * self.visit(l[1])
    '''
    --------------------------------------------------------
    -------------------ESCRITURES------------------
    --------------------------------------------------------
    '''

    def visitPrint(self, ctx: FunxParser.PrintContext):
        l = list(ctx.getChildren())
        i = 2
        while i < len(l) and l[i].getText() != ')':
            if l[i].getText() == '"':
                print(l[i + 1].getText(), end='')
                i += 2
            else:
                print(self.visit(l[i]), end='')
            i += 2
        print('')
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
            while l[i].getText() != '}' and result is None:
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

        self.dictFuncions[idFun] = representacioFuncio(
            idFun, self.visit(l[1]), ctx)
        mostraFuncions.append(l[0].getText()+' '+ " ".join(self.visit(l[1])))

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


resultats = []
mostraFuncions = []
textbox_value =""

visitor = Funx()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', resultats = resultats, funcions = mostraFuncions)

@app.route('/reset', methods=['POST'])
def reset():
    resultats = []
    mostraFuncions = []
    textbox_value =""
    return render_template('base.html', resultats = resultats, funcions = mostraFuncions, error = False)

@app.route('/submit', methods=['POST'])
def submit():
    #funcions = visitor.getFunctions()
    try:
        textbox_value = request.form.get('textbox')
        input_stream = InputStream(textbox_value)

        lexer = FunxLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = FunxParser(token_stream)
        tree = parser.root()
        resultVisit = visitor.visit(tree)

        if len(resultats) >= 5:
            resultats.pop(0)
        resultats.append((textbox_value,resultVisit))
        return render_template('base.html', resultats = resultats, funcions = mostraFuncions)
    except:
        return render_template('base.html', resultats = resultats, funcions = mostraFuncions, error = True)
        



if __name__ =='main':
    app.run()