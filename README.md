# Pràctica compiladors - Funx
---

Lluís Llull Riera 

Professor: Jordi Petit 

Assignatura: Llenguatges de Programació (LP) 2022

[Enunciat de la pràctica](https://github.com/gebakx/lp-funcions)

---
## Introducció

Funx és un llenguatge de programació orientat a expressions i funcions. Amb Funx podem definir funcions i acabar, opcionalment, amb una expressió.

Funx ha estat construït a partir d'*antlr4* i *Python*.
---

## Especificacions

### Expressions

Si una variable encara no ha rebut cap valor, el seu valor és zero. Els operadors aritmètics són els habituals (+, -, *, /, %) i amb la mateixa prioritat que en C. Evidentment, es poden usar parèntesis.

Els operadors relacionals per **comparacions**(=, !=, <, >, <=, >=) retornen 0 per fals i 1 per cert.
### Assignació de variables
L'assignació ha d'avaluar primer l'expressió a la part dreta del `<-` i emmagatzemar després el resultat a la variable local a la part esquerra.
El nom de la variable sempre ha de començar amb minúscula.

    a <- a - b.

### Funcions
En Funx no podem definir programes, només funcions i una expressió final. Podem definir la llista de funcions sense que importi l'ordre.

Cada funció té un nom, paràmetres i un bloc associat. Els blocs es troben inscrits entre els símbols { i }.

Les funcions han de començar per una lletra majúscula i passen els paràmetres per còpia. Retornen el valor de qualsevol expressió que trobin en el seu bloc i en aquell precís instant. A continuació en teniu un exemple:
~~~
Suma x y {
    x + y
}

Torna10 {
    r<-10
    r
}

~~~
***Crida***
a una funció té la semàntica habitual. Si el nombre de paràmetres passats no corresponen als declarats, es produeix un error. Les funcions es poden cridar recursivament. La sintaxi  és sense parèntesis ni comes.

    Suma 2 2
    Out: 4

    Torna10
    Out: 10
### Condicionals
La instrucció condicional té la semàntica habitual. El bloc del *else* és optatiu.
    ~~~
    if x = y { z <- 1 }
    * if x = y { 
        z <- 1 
    } 
    else {
         z <- 2 
    }
    ~~~
### Bucles 
La instrucció iterativa amb while té la semàntica usual.
    ~~~
    while a > 0 {
         a <- a / 2 
    }.
    ~~~


## Funcionalitats extres
1. **Escriptures (print)**:
 Les escritures són una eina molt útil per debugar i depurar el codi.
En Funx les escriptures s'escriuen de la següent forma:

    `print("Això és una escriptura" + variable)`

On es poden concatenar elements amb un *+*, i a més es poden escriure tan variables *var* o text entre cometes *"text"*.

2. **Operacions lògiques:**
+ *AND* -> True si els dos literals són certs => ` litA && litB`
+ *OR* -> True si almenys un literal és cert => `litA && litB`
+ *XOR* -> True si un i només un dels dos literals és true => `litA &| litB`
+ *NOT* -> Nega el proxim literal => ` ! lit`

3. **Bucle for:** implementat de la següent forma:

~~~
for i<-0 ; i < 5 ; i <- i+1 {
    print(i)
}
~~~

4. **Coma flotant:** Per usar nombres decimals en coma flotant just és necessari expresar-los de la següent forma `5.0`, `3.141698`,`2.5`...

---

## Demostració amb un exemple

Amb els jocs de proves podem veure totes les especificacions abans mencionades i també si el seu funcionament és el correcte. Tenim un total de 4 jocs nomenats de la següent forma _test*.funx_. Veurem el cas del joc de proves *test4.funx* per comprovar si es compleix tot el que hem mencionat.

Es tracta d'un programa que pretén comprovar si un nombre x és un *primer perfecte*.  Donat que *s(n)* és la suma dels dígits del nombre n,
un nombre **n** és *primer perfecte* si la seqüència infinita formada per n, s(n), s(s(n))... només conté nombres primers.

En aquesta primera funció on es comprova si un nombre *n* és primer, veiem el funcionament de l'**if**, la **definició de funcions** i el bucle **for**
~~~
IsPrime n {
    if n <= 1 {0}
    else{
        for i<-2 ; i*i < n; i<-i+1 {
            if(n % i) = 0 {0} 
        }
    }
    1
}
~~~
En la següent funció obtenim *s(n)*, és a dir, la suma dels dígits d'un nombre. I hi podem veure el comportament d'un bucle **while** i l'**assignació de variables** en el seu propi context.

~~~
Suma_digits x {
    while x > 0 {
        suma <- suma + (x%10)
        x<- x/10
        a<-x>0
    }
    suma
}
~~~

Finalment, aquesta funció, la qual comprova recursivament si tota la seqüència de s(n) són primers, comprova si el nombre *n* és un primer perfecte.
Aquí podem provar si funciona la **recursivitat**.

~~~
EsPrimePerfecte x {
   if (IsPrime x) = 0 {0}
   if x < 10 {1.
   else {
        n <- (Suma_digits x)
        EsPrimePerfecte n
    }
}

EsPrime Perfecte 977
~~~
    Out:1

Amb aquest programa, que dota de tres funcions, es poden visualitzar molts d'aspectes del nostre llenguatge, com la crida i definició a funcions, bucles, assignació de variables locals, recursivitat, etc.

---
## Limitacions

Funx no deixa de ser un llenguatge molt simple i amb funcionalitats acadèmiques, per això disposa d'una sèrie de limitacions:
1. Crida a funcions on la pròxima línia hi ha una expressió:
En el cas que vulguem cridar una funció, el més convenient, tot i que no sempre és necessari, és cridar tota la funció entre parèntesis de la següent forma.

    (Fibo (n-1)) + (Fibo (n-2))
Ja que si no posem els parèntesis, encara que teòricament no siguin necessaris, el llenguatge no sap diferenciar quan una expressió és o no un paràmetre de la funció.

---
## Conclusió

Puc dir que estic prou satisfet amb la versió final del llenguatge. S'han pogut assolir tots els punts mencionats a l'enunciat, i a més a més,
també he pogut desenvolupar una sèrie de funcionalitats extres que doten el programa d'una major completitud.

Finalment, cal comentar que tot i estar orgullós del resultat, no lleva que ***Funx*** és un llenguatge extremadament simple que no és capaç de realitzar tasques essencials com altres llenguatges actuals. Així i tot, crec que dur a terme aquesta pràctica ha estat una experiència enriquidora molt útil per aprendre i consolidar aspectes teòrics de com funcionen els compiladors i de tots els llenguatges de compilació en general.