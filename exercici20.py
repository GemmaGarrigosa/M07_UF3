
myDict ={}

while True:
    nom = input('Introdueix el nom')
    edat = int(input('Introdueix la edat'))

    myDict[nom] = edat

    resposta = input('Vols continuar? S/N')
    if resposta.lower() == 'n':
        break

print(myDict)



