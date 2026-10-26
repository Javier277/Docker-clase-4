def contar_vocales(palabra):
    contador=0
    palabra=palabra.lower()
    for letra in palabra:
        if letra == "a" or letra == "e" or letra ==  "i" or letra == "o" or letra == "u":
            contador +=1
    return contador
print(contar_vocales("Javier"))


    