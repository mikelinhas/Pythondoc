import mammoth
from bs4 import BeautifulSoup
from tableReader import reader
import xlwt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# LEER EL DOCUMENTO
Tk().withdraw()
filename = askopenfilename()

with open(filename, "rb") as docx_file:
	result = mammoth.convert_to_html(docx_file)
	html = result.value

soup = BeautifulSoup(html, 'html.parser')
error = "está mal formateado el documento prim"


# TRADUCCIONES
ABRAZADERAS = "AFRABN0" # DN "xxx"
BRIDAS = "AACBCU0" # DN "xxx"
BRIDAS_CIEGAS = "AACBCI0" # DN "xxx"
CODOS_BW = "AACCB49" # DN "xxx"
CAPS_BW = "AACCPS0" # DN "xxx"
FILTROS_Y_BRIDAS = "AFIBA40" # DN "xxx"
FILTROS_Y_ROSCADOS = "AFIRBAA" # DN "xxx"
JUNTAS = "AACJGK0" # DN "xxx"
REDUCCIONES = "AACRC" # DNDN "xxxxx"
TES_BW = "AACTIB4" # DN "xxx"
TORNILLOS = "AFRTB" # MxL "xx xxx"
TUERCAS = "AFRT0000" # M "xx"
VALVULA_ARI_MANUAL = "AVLMAB0" # DN "xxx"
VALVULA_CHERO_BRIDAS = "AVLMCB0" # DN "xxx"
VALVULA_CHERO_ROSCADA = "AVLMRA0" # DN "xxx"
VALVULA_RK_ROSCADA = "xxCODIGOxx" # DN "xxx"

OTROS = []


# PREPARAR DATOS PARA DOCUMENTO EXCEL
excelData = []

for heading in soup.find_all("h1"):
	h1_text = heading.get_text()
	h1_sibling = heading.next_sibling
	
	if h1_sibling.name != "table":
		print (error)
		continue

	if h1_text == "CODOS BW":
		result = reader.tablaHorizontal(CODOS_BW, h1_sibling)
		print(h1_text)
		print(result, "\n")
	
	elif h1_text == "CAPS BW":
		result = reader.tablaHorizontal(CAPS_BW, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "BRIDAS":
		result = reader.tablaHorizontal(BRIDAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "BRIDAS CIEGAS":
		result = reader.tablaHorizontal(BRIDAS_CIEGAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "TES BW":
		result = reader.tablaHorizontal(TES_BW, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "CAPS":
		result = reader.tablaHorizontal(CAPS_BW, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "JUNTAS":
		result = reader.tablaHorizontal(JUNTAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "ABRAZADERAS":
		result = reader.tablaHorizontal(ABRAZADERAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "FILTROS Y CON BRIDAS":
		result = reader.tablaHorizontal(FILTROS_Y_BRIDAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "TORNILLOS":
		result = reader.tornillos(TORNILLOS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "TUERCAS":
		result = reader.tuercas(TUERCAS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "TRANSMISORES DE PRESION" or h1_text == "TRANSMISORES DE PRESIÓN":
		result = reader.tablaCodigo3(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "TRANSMISORES DE TEMPERATURA":
		result = reader.tablaCodigo3(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "PURGADORES":
		result = reader.tablaCodigo3(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "VALVULAS NEUMATICAS" or h1_text == "VÁLVULAS NEUMÁTICAS":
		result = reader.tablaCodigo4(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "VALVULAS MOTORIZADAS" or h1_text == "VÁLVULAS MOTORIZADAS":
		result = reader.tablaCodigo4(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "VALVULAS MANUALES DE BRIDAS" or h1_text == "VÁLVULAS MANUALES DE BRIDAS":
		CODIGOS = [VALVULA_ARI_MANUAL, VALVULA_CHERO_BRIDAS]
		result = reader.valvulasManualesBridas(CODIGOS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "VALVULAS MANUALES NPT" or h1_text == "VÁLVULAS MANUALES DE BRIDAS":
		CODIGOS = [VALVULA_CHERO_ROSCADA]
		result = reader.valvulasManualesRoscadas(CODIGOS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "VALVULAS DE BOLA NPT" or h1_text == "VÁLVULAS DE BOLA NPT":
		CODIGOS = [VALVULA_RK_ROSCADA]
		result = reader.valvulasBolaNPT(CODIGOS, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "REDUCCIONES":
		result = reader.reducciones(REDUCCIONES, h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "ANCLAJES":
		result = reader.tablaNormal(h1_sibling)
		print(h1_text)
		print(result, "\n")

	elif h1_text == "ACCESORIO ROSCADO NPT":
		result = []

		while h1_sibling.next_sibling.name == "table":
			result.extend(reader.accesorioNPT(h1_sibling))
			h1_sibling = h1_sibling.next_sibling

		if h1_sibling.name == "table":
			result.extend(reader.accesorioNPT(h1_sibling))

		print(h1_text)
		print(result, "\n")


	else:
		result = []
		OTROS.append(h1_text)

	excelData.extend(result)

print(OTROS)


# PREPARE THE EXCEL
wb = xlwt.Workbook()
ws = wb.add_sheet("Lista de material")
x = 0

ws.write(x, 0, "REFERENCIA BAVIERA")
ws.write(x, 1, "CANTIDAD")

for item in excelData:
	x = x+1
	ws.write(x,0,item[0])
	ws.write(x,1,item[1])

wb.save("Material List.xls")
