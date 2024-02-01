import json
'''

Crear una funció que mostri, per consola, i guardi en un arxiu extern, un JSON amb una key de nom book que contindrà title,
 cover, year i pages. Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values).

'''
titles = ['Title1','Title2','Title3','Title4']
covers = ['cover 1','cover 2','cover 3','cover 4']
year = [1995,1996,1997,1998]
pages =[100,200,300,400]

books = []


def creaJSON ():


    for i in range (4):
        books.append(
            {
                "book":[
                    {
                        "Title": titles[i],
                        "Cover": covers[i],
                        "Year": year[i],
                        "Pages": pages[i]
                    }
                ]
            }
        )
        with open('books.json','w') as f:
            json.dump(books,f,indent=2) #dump demana dades, fitxer

        with open('books.json','r') as f:
            resultat = json.load(f)
            print(json.dumps(resultat,indent=2)) #dumps demana resultat

creaJSON()


