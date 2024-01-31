areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]

print(f'Segon element: {areas_pis[1:2]}')
print(f'Últim element: {areas_pis[-1:]}')
print(f'Àrea de la terrassa: {areas_pis[areas_pis.index("Terrassa")+1]}')
print(f'Del primer element al tercer: {areas_pis[0:3]}')
print(f'Del primer element al ultim {areas_pis[0:]}')
print(f"Total de l'area de ambdues habitacions {(areas_pis[areas_pis.index('Habitació1')+1]+areas_pis[areas_pis.index('Habitació2')+1])}") #amb index
areas_pis[areas_pis.index('Lavabo')+1] = 8.50
print(f'Area del lavabo canviada: {areas_pis[0:]} ')
areas_pis.append('Pati interior')
areas_pis.append(2.78)
print(f"Llista amb pati interior afegit: {areas_pis[0:]}")
print(f"Tota l'àrea del pis: {sum(areas_pis[1::2])}")


