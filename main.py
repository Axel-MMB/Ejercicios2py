#Ejercicios 2
import math


#Ejercicio1

def area_rectangulo(altura, base):
    return altura * base


#Ejercicio2

def area_circulo(radio):
    return math.pi * (radio * radio)

#Ejercicio3

def relacion(a,b):
    if a == b:
        return 0
    if a > b:
        return 1
    else:
        return -1

#Ejercicio4

def intermedio(a,b):
    return b - ((b - a)/2)

#Ejercicio5

def  recortar(numero, limInf, limSup):
    if numero < limInf:
        return limInf
    elif numero > limSup:
        return limInf
    else:
        return numero

#Ejercicio6

pares = []
impares = []
def separar(numero):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)