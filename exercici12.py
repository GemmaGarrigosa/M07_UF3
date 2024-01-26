mesos =('','Gener','Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre') #Les tuples son amb ()

while True:
    numero = int(input('Introdueix un nombre del 1 al 12 (0 per sortir)'))

    if numero == 0:
        break
    else:
        print(f'{mesos[numero]}')