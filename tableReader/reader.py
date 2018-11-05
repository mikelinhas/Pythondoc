def say_hello():
	print("Hello")

# FUNCION PARA LEER LA UNA TABLA NORMAL
def tablaNormal(table):
	rows = table.find_all("tr")
	
	result = []

	for row in rows:
		cols = row.find_all("td")
		descripcion = cols[0].get_text()

		if not cols[1].get_text():
			quantity = 0
		else:
			quantity = int(cols[1].get_text())

		item = [descripcion, quantity]
		result.append(item)

	return result

# FUNCION PARA LEER LA UNA TABLA HORIZONTAL SIMPLE
def tablaHorizontal(codigo, table):
	rows = table.find_all("tr")
	cols_num = len(rows[0].find_all("td"))
	result = []

	for x in range(0,cols_num):
		DNs = rows[0].find_all("td")
		quantitys = rows[1].find_all("td")
		DN = DNs[x].get_text()[2:]

		if not quantitys[x].get_text():
			quantity = 0
		else:
			quantity = int(quantitys[x].get_text())

		if int(DN)<100:
			cod_baviera = codigo + '0' + DN
			item = [cod_baviera, quantity]
			result.append(item)
			#print(cod_baviera, ": ", quantity)
			
		else:
			cod_baviera = codigo + DN
			item = [cod_baviera, quantity]
			result.append(item)
			#print(cod_baviera, ": ", quantity)

	return result

# FUNCION PARA LEER LA UNA TABLA CON CODIGO EN LA 3a COLUMNA
def tablaCodigo3(table):
	rows = table.find_all("tr")
	rows.pop(0)

	result = []

	for row in rows:
		cols = row.find_all("td")
		cod_baviera = cols[2].get_text()
		
		if not cols[3].get_text():
			quantity = 0
		else:
			quantity = int(cols[3].get_text())

		item = [cod_baviera, quantity]
		result.append(item)
		#print(cod_baviera, ": ", quantity)

	return result

# FUNCION PARA LEER LA UNA TABLA CON CODIGO EN LA 4a COLUMNA
def tablaCodigo4(table):
	rows = table.find_all("tr")
	rows.pop(0)

	result = []

	for row in rows:
		cols = row.find_all("td")
		cod_baviera = cols[3].get_text()
		
		if not cols[4].get_text():
			quantity = 0
		else:
			quantity = int(cols[4].get_text())

		item = [cod_baviera, quantity]
		result.append(item)
		#print(cod_baviera, ": ", quantity)

	return result

# FUNCION PARA LEER LOS TORNILLOS
def tornillos(codigo, table):
	rows = table.find_all("tr")

	result = []

	for row in rows:
		cols = row.find_all("td")
		Metric = cols[0].get_text()

		if not cols[1].get_text():
			quantity = 0
		else:
			quantity = int(cols[1].get_text())

		if len(Metric) == 6:
			cod_baviera = codigo + Metric[1:3] + "0" + Metric[4:6]
			item = [cod_baviera, quantity]
		elif len(Metric) == 7:
			cod_baviera = codigo + Metric[1:3] + Metric[4:7]
			item = [cod_baviera, quantity]
		else:
			print("WTF?")
			return "error"

		result.append(item)

	return result

# FUNCION PARA LEER LAS TUERCAS
def tuercas(codigo, table):
	rows = table.find_all("tr")

	result = []

	for row in rows:
		cols = row.find_all("td")
		Metric = cols[0].get_text()
		cod_baviera = codigo + Metric[1:]

		if not cols[1].get_text():
			quantity = 0
			item = [cod_baviera, quantity]
		else:
			quantity = int(cols[1].get_text())
			item = [cod_baviera, quantity]

		result.append(item)

	return result

# FUNCION PARA LEER LA TABLA DE LAS VALVULAS MANUALES CON BRIDAS
def valvulasManualesBridas(codigos, table):

	ari = codigos[0]
	chero = codigos[1]

	rows = table.find_all("tr")
	rows.pop(0)

	result = []

	for row in rows:
		cols = row.find_all("td")
		descripcion = cols[0].get_text().lower()
		DN = cols[1].get_text()[2:]

		if len(DN) < 3:
			DN = "0" + DN

		if not cols[2].get_text():
			quantity = 0
		else:
			quantity = int(cols[2].get_text())

		if descripcion == "ari":
			cod_baviera = ari + DN
			item = [cod_baviera, quantity]

		elif descripcion == "chero":
			cod_baviera = chero + DN
			item = [cod_baviera, quantity]

		else:
			print("error", descripcion, ": ", quantity)
		
		result.append(item)

	return result	

# FUNCION PARA LEER LA TABLA DE LAS VALVULAS MANUALES ROSCADAS
def valvulasManualesRoscadas(codigos, table):

	chero = codigos[0]

	rows = table.find_all("tr")
	rows.pop(0)

	result = []

	for row in rows:
		cols = row.find_all("td")
		descripcion = cols[0].get_text().lower()
		DN = cols[1].get_text()[2:]

		if len(DN) < 3:
			DN = "0" + DN

		if not cols[2].get_text():
			quantity = 0
		else:
			quantity = int(cols[2].get_text())

		if descripcion == "chero":
			cod_baviera = chero + DN
			item = [cod_baviera, quantity]
		else:
			print("error", descripcion, ": ", quantity)

		result.append(item)

	return result

# FUNCION PARA LEER LA TABLA DE LAS VALVULAS DE BOLA NPT
def valvulasBolaNPT(codigos, table):

	rk = codigos[0]

	rows = table.find_all("tr")
	rows.pop(0)

	result = []

	for row in rows:
		cols = row.find_all("td")
		descripcion = cols[0].get_text().lower()
		DN = cols[1].get_text()[2:]

		if len(DN) < 3:
			DN = "0" + DN

		if not cols[2].get_text():
			quantity = 0
		else:
			quantity = int(cols[2].get_text())

		if descripcion == "rk":
			cod_baviera = rk + DN
			item = [cod_baviera, quantity]
		else:
			print("error", descripcion, ": ", quantity)

		result.append(item)

	return result

# FUNCION PARA LEER LA TABLA DE LAS REDUCCIONES
def reducciones(codigo, table):

	rows = table.find_all("tr")

	result = []

	for row in rows:
		cols = row.find_all("td")
		DNxDN = cols[0].get_text()

		if not cols[1].get_text():
			quantity = 0
		else:
			quantity = int(cols[1].get_text())

		if len(DNxDN) == 11:
			DN1 = DNxDN[4:7]
			DN2 = DNxDN[9:]
			cod_baviera = codigo + "0" + DN2 + DN1
			item = [cod_baviera, quantity]

		elif len(DNxDN) == 12:
			DN1 = DNxDN[4:7]
			DN2 = DNxDN[9:]
			cod_baviera = codigo + DN2 + DN1
			item = [cod_baviera, quantity]


		elif len(DNxDN) == 12:
			DN1 = DNxDN[4:8]
			DN2 = DNxDN[10:]
			cod_baviera = codigo + "0" + DN2 + "A"
			item = [cod_baviera, quantity]


		else:
			return ("error", DNxDN)

		result.append(item)

	return result


# FUNCION PARA LEER LA TABLA DE LOS ACCESORIOS NPT
def accesorioNPT(table):

	rows = table.find_all("tr")
	result = []

	for row in rows:
		cols = row.find_all("td")
		descripcion = cols[0].get_text()
		descripcion2 = cols[1].get_text()
		DN = descripcion2[2:]

		if not cols[2].get_text():
			quantity = 0
		else:
			quantity = int(cols[2].get_text())

		if descripcion.lower() == "manguito":
			cod_baviera = "AACM3NA0" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "medio manguito":
			cod_baviera = "AACCMMN3" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "t":
			cod_baviera = "AACTIN30" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "codo h-h":
			cod_baviera = "AACCN3B0" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "codo m-h":
			cod_baviera = "AACCN3A0" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "machon doble" or descripcion.lower() == "machón doble":
			cod_baviera = "AACMDN30" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "tuerca union" or descripcion.lower() == "tuerca unión":
			cod_baviera = "AFRTU3N0" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "tapon macho" or descripcion.lower() == "tapón macho":
			cod_baviera = "AACTP3A0" + DN
			item = [cod_baviera, quantity]

		elif descripcion.lower() == "tapon hembra" or descripcion.lower() == "tapón hembra":
			cod_baviera = "AACTP3B0" + DN
			item = [cod_baviera, quantity]

		else:
			item = [descripcion + " " + descripcion2, quantity]

		result.append(item)

	return result