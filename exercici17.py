frase = input("Introdueix una frase")

frase = frase.replace(" ","")

tupla = tuple(set(frase))

print(tupla)