import codecs
import random

lista = []
resolver = ""
intentos = 0


with open("palabras.txt", "r", encoding="utf8") as palabras:
    palabras_contenido = palabras.readline()
    while len(palabras_contenido) > 0:
        palabras_contenido = palabras_contenido.replace("\n", "").split(" ")
        for i in palabras_contenido:
            if i not in lista and len(i) > 3:
                lista.append(i)
        palabras_contenido = palabras.readline()


def inicio():
    global resolver
    global intentos
    palabra = random.choice(lista)
    print("bienvenido al juego del ahorcado para ganar tienes que adivinar la palabra antes de que se te acaben los intentos")
    intentos = len(palabra) / 3
    intentos = int(intentos) + 2
    resolver = ("_"*int(len(palabra)))
    print(resolver)
    print(intentos)
    adios_tildes(palabra)


def juego(palabra):
    global resolver
    global intentos
    print(palabra)
    letras = set(palabra)
    usado = []
    while len(letras) > 0 and intentos > 0:
        print("te quedan: " + str(intentos) + " intentos has probado con: " + " ".join(usado))
        resolver = [letras if letras in usado else "_" for letras in palabra]
        print("hasta el momento has adivinado:" + " ".join(resolver))
        opcion = input("elige una letra")

        if opcion in usado:
            print("ya habias intentado esa letra")

        if opcion in letras:
            usado.append(opcion)
            letras.remove(opcion)
            print("oh pues " + opcion + " si esta en la plabra")

        else:
            intentos -= 1
            print("lo lamento pero " + opcion + " no esta en la palabra")
            usado.append(opcion)

    if intentos == 0:
        print("oh vaya parece que perdiste pero diste lo mejor y es lo que importa")

    if len(letras) == 0:
        print("genial ganaste se nota que sabes leer")


def adios_tildes(palabra):
    palabra = palabra.replace("à", "a")
    palabra = palabra.replace("è", "e")
    palabra = palabra.replace("ì", "i")
    palabra = palabra.replace("ò", "o")
    palabra = palabra.replace("ù", "u")
    return juego(palabra.lower())


inicio()
