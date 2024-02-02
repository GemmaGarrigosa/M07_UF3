class User:
    # Constructor
    def __init__(self, nom, cognom, edat, rol, email, dni):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.rol = rol
        self.email = email
        self.dni = dni

    #Getters
    def get_nom(self):
        return self.nom
    def get_cognom(self):
        return self.cognom
    def get_edat(self):
        return self.edat
    def get_rol(self):
        return self.rol
    def get_email(self):
        return self.email
    def get_dni(self):
        return self.dni

    #Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_cognom(self,cognom):
        self.cognom = cognom

    def set_edat(self,edat):
        self.edat = edat

    def set_rol(self,rol):
        self.rol = rol

    def set_email(self,email):
        self.email = email

    def set_dni(self,dni):
        self.dni = dni

    def salutacio(self):
        print(f'Nom: {self.nom}')
        print(f'Cognom: {self.cognom}')
        print(f'Edat: {self.edat}')
        print(f'Rol: {self.rol}')
        print(f'Email: {self.email}')
        print(f'DNI: {self.dni}')


    def to_dict(self):
        return {
            "nom":self.nom,
            "cognom":self.cognom,
            "edat": self.edat,
            "rol": self.rol,
            "email": self.email,
            "dni": self.dni
        }



persona = User('Gemma', 'Garrigosa', 28, 'Alumnat', 'gemma.garrigosa@gmail.com', '123456789L')

persona.salutacio()