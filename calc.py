#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def suma(op1, op2):
    """Función que suma los operandos"""
    return op1 + op2


def rest(op1, op2):
    """Función que resta los operandos"""
    return op1 - op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Non numerical parameters")

    if sys.argv[2] == "suma":
        resultado = suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = rest(operando1, operando2)
    else:
        sys.exit("Sólo puede ser suma o resta")
    print(resultado)
