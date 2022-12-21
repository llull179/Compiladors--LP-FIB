Funx: Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4

run: Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g
	python3 funx.py
jocs: Funx.g
	$(info Input per defecte)
	python3 funx.py
	for number in 1 2 3 4 ; do \
		$(info Joc de prova num $$number) \
        python3 funx.py jocs_de_proves/joc$$number.txt ; \
    done
flask: Funx.g
	export FLASK_APP=funx
	flask run