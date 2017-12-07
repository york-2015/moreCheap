#!/usr/bin/python
import os
def title():
	print "======================================================"
	print "==Se rrequiere que conteste una serie de preguntas.==="
	print "===========Disculpe por las molestias.================"
	print "======================================================"
		
class Producto(object):
	def __init__(self, numeroProducto):
		self.numeroProducto = numeroProducto
		print "producto numero %s" % self.numeroProducto
		self.nombreProducto=raw_input("Nombre del producto numero ----%s---- comparar: " % self.numeroProducto) 
		self.total1 = float(raw_input("Precio total del producto  ----%s----: " % self.nombreProducto.upper()))
		
		print "==============================="
		print "==Esta comformato por=================================".upper()
		print "==1) Kilos y gramos======================================"
		print "==2) liquido============================================="
		print "==3) Unidades============================================"
		print "======================================================"
		
		self.pre1 = input("respuesta 1, 3: ")
		if self.pre1 == 1:
			self.compuesto = raw_input("Cantidad en kilos: ")
		elif self.pre1 == 2:
			self.compuesto = raw_input("Cantidad en litros: ")
		elif self.pre1 == 3:
			print "En construccion."
		else:
			print "Su respuesta no es correcta."
	
	def fun_valor_Kilo_minilitro(self):
		precioxquilo = float(self.total1/self.compuesto)
		precioxgramo = float(precioxquilo/1000 )
		#eleccion en minilitros
		pri_kilo="{0:.3f}".format(precioxquilo)
		pri_gramo="{0:.3f}".format(precioxgramo)
		print "%s %s \n%s %s" %(pri_kilo, self.nombreProducto, pri_gramo, self.nombreProducto)
def main(var_respuesta):	
	#ordenar esto
	if var_respuesta == 1:
		producto1=Producto(1)
	elif var_respuesta == 2:
		producto1=Producto(1)
		producto2=Producto(2)
		producto1.fun_valor_Kilo_minilitro()
		producto2.fun_valor_Kilo_minilitro()
	elif var_respuesta == 3:
		producto2=Producto(1)
		producto2=Producto(2)
		producto2=Producto(3)
		producto1.fun_valor_Kilo_minilitro()
		producto2.fun_valor_Kilo_minilitro()
		producto3.fun_valor_Kilo_minilitro()		
	elif var_respuesta == 4:
		producto2=Producto(1)
		producto2=Producto(2)
		producto2=Producto(3)
		producto2=Producto(4)
		producto1.fun_valor_Kilo_minilitro()
		producto2.fun_valor_Kilo_minilitro()
		producto3.fun_valor_Kilo_minilitro()
		producto4.fun_valor_Kilo_minilitro()
	elif var_respuesta == 5:
		producto1=Producto(1)
		producto2=Producto(2)
		producto3=Producto(3)
		producto4=Producto(4)
		producto5=Producto(5)
		producto1.fun_valor_Kilo_minilitro()
		producto2.fun_valor_Kilo_minilitro()
		producto3.fun_valor_Kilo_minilitro()
		producto4.fun_valor_Kilo_minilitro()
 		producto5.fun_valor_Kilo_minilitro()
		#-----------inicio del menu 

os.system('clear')
while True:
	#cantidad de listas posibles
	titulos=title()
	
	try:

		var_respuesta=input("Cantidad de productos que desea comparar.(1,5): ")
		inicio=main(var_respuesta)
	except NameError:
		raw_input("solo puede poner numero, press enter".upper())
		os.system('clear')
	


