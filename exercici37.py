ftotal = float(input('Introdueix el preu de tot el carrito: '))
iva = 21

def amb_iva(ftotal, iva):
    ftotal = ftotal +(ftotal * (iva/100))
    return ftotal

print(amb_iva(ftotal, iva))

