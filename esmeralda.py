dicionario = {}

stringConhecida = input("").upper()
stringCifrada = input("").upper()

msgCifrada = input("").upper()
msgDecifrada = ""

for c in range(len(stringCifrada)):

    dicionario.update({stringCifrada[c] : stringConhecida[c]})

for c in range(len(msgCifrada)):

    if(msgCifrada[c] not in dicionario):
        msgDecifrada += '.'
    else:
        msgDecifrada += dicionario[msgCifrada[c]]

print(msgDecifrada)

