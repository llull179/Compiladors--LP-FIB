Funx: Funx.g
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g

run: Funx.g
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g
	python3 funx.py
flask: Funx.g
	export FLASK_APP=funx
	flask run