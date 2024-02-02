def llista_quadrat(llista):
    nova_llista = []
    for i in llista :
        valor = llista[i]
        nova_llista.append(valor**2) #potencia de 2

    print(nova_llista)