text = input('Introdueix entre 1 i 3 paraules')

text = text.split() #Genera un array amb cada paraula separada

for paraula in text:
    print(f"Paraula: {paraula}")
    print(f"Llongitut: {len(paraula)}")
    print(f"Primer caràcter: {paraula[0]} ")
    print(f"Últim caracter: {paraula[-1]}")