grammar Funx;

root : codi EOF ;

codi: (print | definicioFuncio)* (print|expr|comparacio)?;

instr: assignacio
    | condicional
    | bucle
    | definicioFuncio
    | expr
    | comparacio
    | print
    ;

//CONDICIOANLS
condicional: IF comparacio '{' instr* '}'                   #IfThen
        | IF comparacio '{' instr* '}' ELSE '{' instr* '}'  #IfThenElse
        ;

//COMPARACIO
comparacio: '(' comparacio ')'  #BracketsComp
        |comparacio AND comparacio                  #And
        | comparacio OR comparacio                  #Or
        | comparacio XOR comparacio                 #Xor
        | NOT comparacio                            #Not
        | expr DIF expr                             #Dif
        | expr EQ expr                              #Eq
        | expr MAJEQ expr                           #Majeq
        | expr MENEQ expr                           #Meneq
        | expr MAJ expr                             #Maj
        | expr MEN expr                             #Men
        ;

//BUCLES
bucle: WHILE comparacio '{' instr* '}'                             #bucleWhile
    | FOR assignacio ';' comparacio ';' assignacio '{' instr* '}'  #bucleFor
    ;

//ASSIGNACIONS
assignacio: TXT ASSIG (expr|comparacio)         #Assig
;        

//ESCRITURA
print: PRINT '(' ((expr|'"'cjtParams'"')('+' (expr |'"'cjtParams'"'))*)? ')';     

//EXPRESIONS
expr: '(' expr ')'                              #Brackets
    | REST expr                                 #ValorIntNeg
    | TXTFUN cjtExpr                            #FuncioCall
    |<assoc=right> expr POW expr                #Potencia
    | expr MULT expr                            #Multiplicacio
    | expr DIV expr                             #Divisio
    | expr MOD expr                             #Modul
    | expr MES expr                             #Suma
    | expr REST expr                            #Resta
    | INT                                       #ValorInt
    | FLOAT                                     #ValorFloat
    | TXT                                       #Variable
    ;

//DECLARACIÓ FUNCIONS
definicioFuncio: TXTFUN cjtParams '{' instr* '}';

cjtParams: TXT*;

cjtExpr: expr*;

PRINT: 'print';

IF : 'if';
ELSE:'else';

WHILE:'while';
FOR: 'for';

FLOAT: INT+ '.' INT*;
INT : [0-9]+ ;

TXTFUN:[A-Z]+[a-zA-Z_0-9]*;
TXT:[a-z]+[a-zA-Z_0-9]*;

AND:'&&';
OR:'||';
XOR:'|&';
NOT:'!';

DIF: '!=';
EQ: '=';
MAJEQ: '>=';
MENEQ: '<=';
MAJ:'>';
MEN:'<';

ASSIG:'<-';

MES : '+' ;
MULT:'*' ;
REST:'-';
DIV:'/';
POW:'**';
MOD:'%';


COMMENT : '#' ~[\r\n]* -> skip;

WS : [ \n\r]+ -> skip; 