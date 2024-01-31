numeros = input('Introdueix 10 nombres separats per un espai')
llista_numeros = numeros.split(" ")
suma_numeros = 0
contador = 0
for num in llista_numeros:
    suma_numeros += int(num)
    contador+=1



print(f"Números de l'usuari:{llista_numeros}")
print(f'Suma total: {suma_numeros}')
print(f'Mitjana: {suma_numeros / contador}')
