def add_time(start, duration, day=False):
    a = start.split(" ")
    b = a[0].split(":")
    c = duration.split(":")
    hora2 = c[0]
    minuto2 = c[1]
    hora1 = b[0]
    minuto1 = b[1]
    tempo = a[1]
    contador_tempo = 0
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    dian = 0

    horas = int(hora1) + int(hora2)
    minutos = int(minuto1) + int(minuto2)

    while minutos > 60:
        minutos = minutos - 60
        horas = horas + 1

    if tempo == "AM":
        contador_tempo = 1
    else:
        contador_tempo = 2

    while horas > 12:
        horas = horas - 12
        contador_tempo = contador_tempo + 1

    if horas == 12:
        contador_tempo = contador_tempo + 1

    if contador_tempo % 2 == 0:
        tempo = "PM"
    else:
        tempo = "AM"
    if tempo == "PM":
        contador_d = int(contador_tempo / 2)
        contador_d = contador_d - 1
    else:
        contador_d = int(contador_tempo / 2)

    if day:
        day = day.lower()
        dian = days.index(day)
        dian = dian + contador_d
        while dian > 6:
            dian - 6

        dia = days[dian]

    if minutos < 10:
        minutos = "0" + str(minutos)

    if horas < 10:
        horas = "0" + str(horas)

    new_time = (str(horas) + ":" + str(minutos) + " " + (tempo))

    if day:
        new_time = new_time + dia

    if contador_d > 0:
        if contador_d == 1:
            new_time = new_time + " (next day)"
        else:
            new_time = new_time + " (" + str(contador_d) + " days later)"

    return new_time