#!/usr/bin/python
import os 
def fun_tittle():
	print "======================================================"
	print "==Se rrequiere que conteste una serie de preguntas.==="
	print "===========Disculpe por las molestias.================"
	print "======================================================"
def fun_cual_es_mas_barato(precioConocidos, precio_nuevo):
	cal = int(precioConocidos - precio_nuevo)
	if cal > 0:
		print "Es barato, compralo %i " % precioConocidos
	elif cal == 0:
		print "Tienen el mismo valor " 
	elif cal < 0:
		print "El producto es menor. %i " % precioConocidos

def fun_dame_valor_porKilo(kilos, total, kom):
	precioxquilo = total/kilos
	precioxgramo = precioxquilo/1000 
	#eleccion en minilitros
	pri_mini="{0:.3f}".format(precioxquilo)
	pri_mini="{0:.3f}".format(precioxgramo)

def fun_preguntar_basico():
	total = int(raw_input("Precio del prducto a comparar: "))
	kilos = int(raw_input("Peso tu producto(kilos): "))
	siono = raw_input("Este producto se divide en unidade (y/n): ")
	if siono == "y":
		mont_unity = int(raw_input("Dime la cantidad de unidades: "))
	elif siono == "n":
		print "Anotado tiene cero unidades."
		mont_unity = int(0)
	else:
		print 'error'
#-----------inicio del menu 
def menu():
	print "======================================================"
	print "============1- Cual es mas barato.========================="
	print "============2- Comparar precio por kilo.=============="
	print "============3- Comparar por minilitros.===================="
	print "============4- Sacar el precio por unidad. =============="
	print "======================================================"
	res_menu = int(raw_input("Cual es tu respuesta: "))
	os.system('clear')
	
	if res_menu == 1: 		
		mas_barato=fun_cual_es_mas_barato(precio_nuevo, total)
	elif res_menu == 2: 
		print "obtener el valor de un kilo de mi producto. "
		yafun=fun_dame_valor_porKilo(kilos, total)
	elif res_menu == 3:
		minilitros=fun_dame_valor_porkilo(minilitros, total)
 	elif res_menu == 4:
 		unidad=fun_dame_valor_porKilo(unidad, total)
	else:
		print "ERROR"	
		var_menu=menu()

while True:
	var_title=fun_tittle()
	var_preguntas=fun_preguntar_basico()
	var_menu=menu()



