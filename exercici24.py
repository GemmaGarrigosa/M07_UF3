'''
Crear una funció que llegeixi el JSON de l’exercici anterior  i surti el resultat (en format json) per consola.
'''

import json

def llegeixJSON():

    with open("books.json",'r') as f:
        resultat = json.load(f)
        print(json.dumps(resultat,indent=2))

llegeixJSON()