contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
    else:
        print(f'El contacte a eliminar no existeix')
    return contactes

print(elimina(contactes, 'Roger'))

