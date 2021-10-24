import random
caracteres = """!"#$%&'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
n = int(input("numero de claves \n"))
n2 = int(input("largo de las claves"))
contador = 0
contador2 = 0

for clave in range(n):
 claves = ""
 for caracter in range(n2):
  claves += random.choice(caracteres)
 print(claves)