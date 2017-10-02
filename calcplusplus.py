#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

fichero = sys.argv[1]
with open(fichero) as fich:
    fichero = csv.reader(fich)
    calcplus = calcoohija.CalculadoraHija()

    for line in fichero:
        operations = line[0]
        datos = line[1:]
        result = int(datos[0])

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
