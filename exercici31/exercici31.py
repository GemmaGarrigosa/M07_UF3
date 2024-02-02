def calcula_factura(quantitat,iva):
    if iva == 4 or iva == 10 or iva ==21:
        iva = iva
    else:
        iva = 21

    print(f'Valor sense iva: {quantitat} \n'
          f'Valor del IVA: {quantitat * (iva/100)} \n'
          f'Valor amb IVA: {quantitat +(quantitat * (iva/100))}')