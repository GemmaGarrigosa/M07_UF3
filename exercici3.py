primer = input('Introdueix primer valor:')
segon = input('Introdueix segon valor:')

if primer > segon:
    print(f'{primer} és més gran que {segon}')
elif primer < segon:
    print(f'{segon} és més gran que {primer}')
else:
    print('Són iguals')