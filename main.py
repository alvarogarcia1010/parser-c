from utilities.semantic import analizador_semantico
from utilities.types import Types
from utilities.lexer import readSource
from utilities.identificador import Identificador
from grammar.parsingTable import parsingTable
from grammar.parsingTable import terminales

tokenSymbols = list()
parserTokens = list()

tokens = readSource('./Examples/SuccessfulExample.c')
#tokens = readSource('./Examples/FailedExample.c')

for token in tokens:
  if token.type not in [Types.SPACE]:
    parserTokens.append(token.type.name)           
    tokenSymbols.append(token.value)

#Instanciación de la pila
stack = ['EOF', 0]

#Funciones
def buscar_en_tabla(no_terminal, terminal):
	for i in range(len(parsingTable)):
		if( parsingTable[i][0] == no_terminal and parsingTable[i][1] == terminal):
			return parsingTable[i][2]

def agregar_pila(produccion):
	for elemento in reversed(produccion):
		if elemento != 'vacia':
			stack.append(elemento)

x = stack[-1]
position = 0
numberOfLine = 1

syntaxErrors = []

print('<---- Analizador sintáctico ---->')

while (len(stack) > 0):
	if x == parserTokens[position] and x == 'EOF':
		if (len(syntaxErrors) != 0):
			print("Fallo al compilar:")
			for error in syntaxErrors:
					print(error)
		else:
			print("Programa compilado con exito")
			analizador_semantico(tokens)
		break
	else:
		if x == parserTokens[position] and x != 'EOF':
			stack.pop()
			x = stack[-1]
			position += 1

		if x in terminales and x != parserTokens[position]:
			if parserTokens[position] == 'LINE_BREAK' or parserTokens[position] == 'COMENT_LINE':
				parserTokens.pop(position)
				tokenSymbols.pop(position)
				numberOfLine += 1
			else:
				parserTokens.insert(position, x)
				syntaxErrors.append('ERROR EN LÍNEA NUMERO: ' + str(numberOfLine) + ' se esperaba el token '+ str(x) + ' luego de ' + '"' + str(tokenSymbols[position-1]) + '"')
		if x not in terminales:
			celda = buscar_en_tabla(x, parserTokens[position])
			if  celda is None:
				if parserTokens[position] == 'LINE_BREAK' or parserTokens[position] == 'COMENT_LINE':
					parserTokens.pop(position)
					tokenSymbols.pop(position)
					numberOfLine += 1
				else:
					syntaxErrors.append("ERROR EN LÍNEA NUMERO: " + str(numberOfLine) + " no se esperaba "+ str(parserTokens[position]))
					parserTokens.pop(position)
					tokenSymbols.pop(position)
			else:
				stack.pop()
				agregar_pila(celda)
				x=stack[-1]
	#print(stack)
