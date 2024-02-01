'''
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
Un root de nom students.
Cinc childs (del root) amb nom student.
Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
El text de cada etiqueta serà de la vostra elecció.
'''

import xml.etree.ElementTree as ET

def crea_XML():

    noms = ['Gemma','Adrià','Oscar','Joana','Veronica']
    cognoms =['Garrigosa','Garcia','Perez','Lin','Cartagena']
    emails = ['gemma@estudiant.com','adria@estudiant.com','oscar@estudiant.com','joana@estudiant.com','veronica@estudiant.com']
    dnis = ['12345678G','12345678A','12345678O','12345678J','12345678V']

    root = ET.Element('students') #Indiquem i creem l'arrel del XML

    # Creem 5 estudiants
    for i in range(5):
        student = ET.SubElement(root, 'student')

        # Fills de student
        name = ET.SubElement(student, 'name')
        name.text = str(noms[i])

        surname = ET.SubElement(student, 'surname')
        surname.text = str(cognoms[i])

        email = ET.SubElement(student, 'email')
        email.text = str(emails[i])

        dni = ET.SubElement(student, 'dni')
        dni.text = str(dnis[i])

    ET.indent(root) # Identem el xml
    ET.dump(root)  # Per mostrar per consola

    # Guardem el XML a un fitxer
    tree = ET.ElementTree(root)
    tree.write("students.xml") #Crea el xml amb aquest nom

crea_XML()
