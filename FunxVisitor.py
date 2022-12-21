# Generated from Funx.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#codi.
    def visitCodi(self, ctx:FunxParser.CodiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#instr.
    def visitInstr(self, ctx:FunxParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IfThen.
    def visitIfThen(self, ctx:FunxParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IfThenElse.
    def visitIfThenElse(self, ctx:FunxParser.IfThenElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Dif.
    def visitDif(self, ctx:FunxParser.DifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Not.
    def visitNot(self, ctx:FunxParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#BracketsComp.
    def visitBracketsComp(self, ctx:FunxParser.BracketsCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Or.
    def visitOr(self, ctx:FunxParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#And.
    def visitAnd(self, ctx:FunxParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Maj.
    def visitMaj(self, ctx:FunxParser.MajContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Men.
    def visitMen(self, ctx:FunxParser.MenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Majeq.
    def visitMajeq(self, ctx:FunxParser.MajeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Xor.
    def visitXor(self, ctx:FunxParser.XorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Eq.
    def visitEq(self, ctx:FunxParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Meneq.
    def visitMeneq(self, ctx:FunxParser.MeneqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#bucleWhile.
    def visitBucleWhile(self, ctx:FunxParser.BucleWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#bucleFor.
    def visitBucleFor(self, ctx:FunxParser.BucleForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Assig.
    def visitAssig(self, ctx:FunxParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Suma.
    def visitSuma(self, ctx:FunxParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Variable.
    def visitVariable(self, ctx:FunxParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Brackets.
    def visitBrackets(self, ctx:FunxParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ValorInt.
    def visitValorInt(self, ctx:FunxParser.ValorIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Divisio.
    def visitDivisio(self, ctx:FunxParser.DivisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#FuncioCall.
    def visitFuncioCall(self, ctx:FunxParser.FuncioCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Multiplicacio.
    def visitMultiplicacio(self, ctx:FunxParser.MultiplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Modul.
    def visitModul(self, ctx:FunxParser.ModulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ValorFloat.
    def visitValorFloat(self, ctx:FunxParser.ValorFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Potencia.
    def visitPotencia(self, ctx:FunxParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Resta.
    def visitResta(self, ctx:FunxParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#definicioFuncio.
    def visitDefinicioFuncio(self, ctx:FunxParser.DefinicioFuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#cjtParams.
    def visitCjtParams(self, ctx:FunxParser.CjtParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#cjtExpr.
    def visitCjtExpr(self, ctx:FunxParser.CjtExprContext):
        return self.visitChildren(ctx)



del FunxParser