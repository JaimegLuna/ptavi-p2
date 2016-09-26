#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

fichero = sys.argv[1]
with open(fichero) as fich:

    fichero = csv.reader(fich)
    calcplus = calcoohija.CalculadoraHija()

    for linea in fichero:
        operaciones = linea[0]
        datos = linea[1:]
        result = int(datos[0])

        if operaciones == "suma":
            print("Resultado suma = ")
            for n in range(1, len(datos)):
                result = calcplus.suma(result, int(datos[n]))
        elif operaciones == "resta":
            print("Resultado resta = ")
            for n in range(1, len(datos)):
                result = calcplus.resta(result, int(datos[n]))
        elif operaciones == "multiplicacion":
            print("Resultado multiplicacion = ")
            for n in range(1, len(datos)):
                result = calcplus.multi(result, int(datos[n]))
        elif operaciones == ("division"):
            print("Resultado division = ")
            for n in range(1, len(datos)):
                if datos == "0":
                    result = ("Error: Division by 0 is not allowed")
                else:
                    result = calcplus.divi(result, int(datos[n]))
        else: 
            sys.exit('operaciones posibles: suma, resta, multiplicacion o division')
        print(result)
