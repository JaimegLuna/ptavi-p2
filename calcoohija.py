#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo 


class CalculadoraHija (calcoo.Calculadora):
    def multi(self, op1, op2):
        return op1 * op2

    def divi(self, op1, op2):
        return op1 / op2
if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        calculadorahija = CalculadoraHija()

    if sys.argv[2] == "multiplicacion":
        result = calculadorahija.multi(operando1, operando2)
    elif sys.argv[2] == "division":
            if operando2 == 0:
                result = "Error: Division by 0 is not allowed"
            else:
                result = calculadorahija.divi(operando1, operando2)
    elif sys.argv[2] == "suma":
        result = calculadorahija.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadorahija.resta(operando1, operando2)
    else:
        sys.exit('solo se puede suma, resta, multiplicacion o division')
    print(result)
