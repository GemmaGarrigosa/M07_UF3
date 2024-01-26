paraules = input('Introdueix dues paraules')

paraules = paraules.replace(" ","")

tupla = tuple(paraules)

lletres = {} # guardem el contador de cada lletra

for lletra in tupla:
    if lletra in lletres:
        lletres[lletra] +=1
    else:
       lletres[lletra] =1


for lletra in lletres:
    comptador = lletres[lletra]
    print(f'{lletra}: {comptador}')