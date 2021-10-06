import discord
import requests
import json
import random

client = discord.Client()
respuesta = ""
malo = ["trolo",
        ]

triste = ["triste", "deprimido", "melancolico", "infeliz", "sad", "miserable", "enojado", "unhappy", "depressed",
          "depressing"]

alegrar = [
    "alegrate <3",
    "aguanta firme",
    "eres una gran persona / bot!",
]

suerte = ["examen",
          "final",
          "trimestal",
          "practico",
          "evaluativo", ]

comandos = [
    "?",
    "?hello",
    "?inspira",
    "triste",
    "deprimido",
    "melancolico",
    "infeliz",
    "sad",
    "miserable",
    "enojado",
    "unhappy",
    "depressed",
    "depressing",
    "comandos",
    "?nuevo_",

]

with open("alegre_lista.txt", "r") as alegre:
    alegre_contenido = alegre.readline()
    while len(alegre_contenido) > 0:
        if alegre_contenido not in alegrar:
            alegrar.append(alegre_contenido)
        alegre_contenido = alegre.readline()

with open("malo.txt", "r") as malos:
    malo_contenido = malos.readline()
    while len(malo_contenido) > 0:
        print(malo)
        if malo_contenido not in malo:
            malo.append(malo_contenido.replace("\n", ""))
        malo_contenido = malos.readline()


def puteada():
    global respuesta
    respuesta = "no te hagas el chistoso la concha de tu hermana"
    return respuesta


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith("?hello"):
        await message.channel.send("!hello master")

    elif msg.startswith("?inspira"):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in triste):
        await message.channel.send(random.choice(alegrar))

    if msg.startswith("?comandos"):
        await message.channel.send(comandos)

    if msg == "?":
        await message.channel.send("?comandos para una lista de comandos")

    if any(word in msg for word in suerte):
        await message.channel.send("suerte, ojala apruebes y  si no bueno a entregar la cola al profe")

    if msg.startswith("?nuevo_"):
        await message.channel.send("procesando")
        actualizar(msg)
        await message.channel.send(respuesta)


def actualizar(msg):
    global respuesta
    partes = []
    partes = msg.split("_")
    partes.remove("?nuevo")
    msg = "".join(partes)
    if any(word in msg for word in malo):
        puteada()
    else:
        with open("alegre_lista.txt", "a") as joda:
            joda.write(msg + " \n")
        respuesta = "your message has been upload"
        return respuesta


client.run("")
