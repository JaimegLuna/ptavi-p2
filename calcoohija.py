#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo 

class CalculadoraHija(calcoo.Calculadora):

	def mult(self, op1, op2):
		return op1 * op2

	def div(self, op1, op2):
		return op1 / op2

if __name__ == "__main__":
	
	calculadorahija = CalculadoraHija()

	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "multiplicación":
		resultado = calculadorahija.mult(operando1, operando2)
	elif sys.argv[2] == "división":
		if operando2 == 0:
			resultado = "Error: No se puede dividir entre 0"
		else:
			resultado = calculadorahija.div(operando1, operando2)
	elif sys.argv[2] == "suma":
		resultado = calculadorahija.suma(operando1, operando2)
	elif sys.argv[2] == "rest":
		resultado = calculadorahija.rest(operando1, operando2)
	else:
		sys.exit('Sólo se puede multiplicación, división, suma o resta')

	print(resultado)
	

		
	
