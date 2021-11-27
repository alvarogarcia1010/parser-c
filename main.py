from utilities.semantic import analizador_semantico
from utilities.types import Types
from utilities.lexer import readSource
from utilities.identificador import Identificador
from grammar.parsingTable import parsingTable
from grammar.parsingTable import terminales

identifiers = list()
tokenSymbols = list()
parserTokens = list()

isIdentifierType = False
isAssignmentType = False
isVarType = False
tokenValue = ''

indexTokenV1 = 0
indexToken = 0
counter = 0

tokens = readSource('./Examples/SuccessfulExample.c')
#tokens = readSource('./Examples/FailedExample.c')

for token in tokens:
  if token.type not in [Types.SPACE]:
    # Llenamos la lista que le pasaremos al parser
    parserTokens.append(token.type.name)           
    tokenSymbols.append(token.value)

    if (token.type == Types.FLOAT or token.type == Types.INT):
      isVarType = True
      indexTokenV1 = tokens.index(token)

    if (token.type == Types.IDENTIFIER and tokens.index(token)-2 == indexTokenV1):
      isIdentifierType = True
      tokenValue = token.value
      indexToken = tokens.index(token)

    if (token.type == Types.ASIGNACION and tokens.index(token)-2 == indexToken):
      isAssignmentType = True

    if (token.type == Types.INT_VAL or token.type == Types.FLOAT_VAL or token.type == Types.BOOLEAN_VAL and isAssignmentType):
      identifier = Identificador(tokenValue, token.value, token.type)
      identifiers.append(identifier)
      isVarType = False
      isIdentifierType = False
      isAssignmentType = False

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

x = stack[-1] #primer elemento de der a izq
position = 0
numberOfLine = 1

syntaxErrors = []

while (len(stack) > 0):
	if x == parserTokens[position] and x == 'EOF':
		#Estructura if creada para imprimir los syntaxErrors si los hay, o sino mostrar que no
		if (len(syntaxErrors) != 0):
			print("Fallo al compilar:")
			for error in syntaxErrors:
					print(error)
		else:
			print("Programa compilado con exito")
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

print('<---- Analizador semántico ---->')
analizador_semantico(tokens)
