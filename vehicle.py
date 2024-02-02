'''
Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

'''

class Vehicle:
    # Constructor
    def __init__(self, marca, color, num_portes, cavalls, velocitat_max, preu):
        self.marca = marca
        self.color = color
        self.num_portes = num_portes
        self.cavalls = cavalls
        self.velocitat_max = velocitat_max
        self.preu = preu

    #Getters
    def get_marca(self):
        return self.marca
    def get_color(self):
        return self.color
    def get_num_portes(self):
        return self.num_portes
    def get_cavalls(self):
        return self.cavalls
    def get_velocitat_max(self):
        return self.velocitat_max
    def get_preu(self):
        return self.preu

    #Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_color(self,color):
        self.color = color

    def set_num_portes(self,num_portes):
        self.num_portes = num_portes

    def set_cavalls(self,cavalls):
        self.cavalls = cavalls

    def set_velocitat_max(self,velocitat_max):
        self.velocitat_max = velocitat_max

    def set_preu(self,preu):
        self.preu = preu

    def parts(self):
        print(f'Marca: {self.marca}')
        print(f'Color: {self.color}')
        print(f'Nº Portes: {self.num_portes}')
        print(f'Cavalls: {self.cavalls}')
        print(f'Velocitat màxima: {self.velocitat_max}')
        print(f'Preu: {self.preu}')


    def to_dict(self):
        return {
            "marca":self.marca,
            "color":self.color,
            "num_portes": self.num_portes,
            "cavalls": self.cavalls,
            "velocitat_max": self.velocitat_max,
            "preu": self.preu
        }



cotxe = Vehicle('BMW', 'Blau', '4', 200, 130, 100000)

cotxe.parts()