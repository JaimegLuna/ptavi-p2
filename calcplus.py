#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open('ficherooperations', 'r')
fichero = fichero.readlines()

if __name__ == "__main__":

    calcplus = calcoohija.CalculadoraHija()

    for line in fichero:
        operations = line.split(',')[0]
        datos = line.split(',')[1:]
        resultado = int(datos[0])

        if operations == "multiplicación":
            print("resultado multiplicación = ")
            for n in range(1, len(datos)):
                resultado = calcplus.multi(resultado, int(datos[n]))

        elif operations == "división":
            print("resultado división = ")
            for n in range(1, len(datos)):
                if datos == "0":
                    resultado = ("Error: no se puede dividir por 0")
                else:
                    resultado = calcplus.div(resultado, int(datos[n]))
        elif operations == "suma":
            print("resultado suma = ")
            for n in range(1, len(datos)):
                resultado = calcplus.suma(resultado, int(datos[n]))

        elif operations == "resta":
            print("resultado resta = ")
            for n in range(1, len(datos)):
                resultado = calcplus.rest(resultado, int(datos[n]))
        else:
            sys.exit("sólo puede ser multiplicación, división, suma o resta")

        print(resultado)
