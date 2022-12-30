from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from EvalVisitor import EvalVisitor
import sys


# Lectura mitjançant un fitxer

if len(sys.argv) < 2:
    default_in = 'default_input.funx'
else:
    default_in = sys.argv[1]
    
input_stream = FileStream(default_in, encoding='utf-8')

lexer = FunxLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = FunxParser(token_stream)
tree = parser.root()

visitor = EvalVisitor()
result = visitor.visit(tree)
# print(tree.toStringTree(recog=parser))