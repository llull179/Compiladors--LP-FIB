Funx: Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4

txt: Funx_txt.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx_txt.g4
	
jocs: Funx_txt.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx_txt.g4
	$(info Input per defecte)
	python3 funx.py
	for number in 1 2 3 4 ; do \
		$(info Joc de prova num $$number) \
        python3 funx.py jocs_de_proves/test$$number.funx ; \
    done
flask: Funx.g
	export FLASK_APP=funx
	flask run