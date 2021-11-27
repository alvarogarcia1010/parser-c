from utilities.types import Types

def analizador_semantico(tokens):
	print('<---- Analizador semántico ---->')
	listtokens = []
	asignaciones = []

	for token in tokens:
		if token.type not in [Types.SPACE, Types.LINE_BREAK, Types.COMENT_BLOCK, Types.COMENT_LINE]:
			listtokens.append(token)
	
	tabla = []
	tipos = []
	lineas = []
	lineasOtrasAsignaciones = []
	it = iter(listtokens)
	next(it)
	add = False
	addid = False
	addif = False
	auxline = []
	auxasig = []

	while True:
		try: 
			curr = next(it)
		except:
			break

		if add:
			auxline.append(curr)
		if addid:
			auxasig.append(curr)
		if curr.value == "int" or curr.value == "float" or curr.value == "char":
			add = True
			auxline.append(curr)
		if curr.type == Types.IDENTIFIER and not add and not addid and not addif:
			addid = True
			auxasig.append(curr)
		if curr.value == 'if':
			addif = True
		if curr.value == '{' and addif:
			addif = False
		if curr.value == ";" and add == True:
			lineas.append(auxline)
			auxline = []
			add = False
		if curr.value == ";" and addid == True:
			lineasOtrasAsignaciones.append(auxasig)
			lineas.append(auxasig)
			auxasig = []
			addid = False

	for l in lineas:
		index = []
		anterior = 0
		isbracket = False
		for i,val in enumerate(l):
			if val.value == "{":
				isbracket = True
			if val.value == "}" and isbracket:
				isbracket = False
			if val.value == "," and not isbracket:
				index.append(i)
					
		for i in index:
			app = None
			if anterior != 0:
				app = [l[0]] + l[anterior+1:i]
			else:
				app = l[anterior:i]
			asignaciones.append(app)
			anterior = i
		app = None
		if anterior != 0:
			app = [l[0]] + l[anterior+1:-1]
		else:
			app = l[anterior:-1]
		
		asignaciones.append(app)
  
	for asig in asignaciones:
		if asig[0].value == 'int' or asig[0].value == 'char' or asig[0].value == 'float':
			if asig[1].value in tabla:
				error = "La variable " + asig[1].value + " ya ha sido declarada"
				print(error)
				#raise Exception(error)
			else:
				tabla.append(asig[1].value)
				tipos.append(asig[0].value)
			if len(asig) > 2:
				apos = False
				for i in range(2,len(asig)):
					if asig[i].type == Types.APOSTROFE:
						apos = not apos
					if asig[i].type == Types.IDENTIFIER and not apos:
						if asig[i].value not in tabla:
							error = "La variable " + asig[i].value + " nunca ha sido declarada"
							print(error)
							#raise Exception(error)
		if asig[0].type == Types.IDENTIFIER:
			apos = False
			for i in range(1,len(asig)):
				if asig[i].type == Types.APOSTROFE:
					apos = not apos
				if asig[i].type == Types.IDENTIFIER:
					if asig[i].value not in tabla:
						error = "La variable " + asig[i].value + " nunca ha sido declarada"
						print(error)
						#raise Exception(error)
	print("<---- Codigo intermedio ----->")    
	for k in asignaciones:
		print(k)
    
	


    
   

    
    

