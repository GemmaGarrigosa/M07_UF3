llista_nombres = []

while True:
    nombres = input('Introdueix els nombres que vulguis (per acabar posa un 0:')
    nombres = nombres.split()

    for nombre in nombres:
        num = int(nombre)
        llista_nombres.append(num) #les tuples son inmutables, primer guardem en un array

    if 0 in llista_nombres:
        break #si hi ha un 0 s'acaba
    tupla =  tuple(sorted(llista_nombres))
    print(tupla)