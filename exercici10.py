
import random
escollit = random.randint(1,100)
intents = 0


while True:
    numero = int(input('Introdueix un numero'))

    if numero <= 100 and numero >= 1:
        if escollit > numero:
            print(f'El nombre és més gran que {numero}')
        elif escollit < numero:
            print(f'El nombre és més petit que {numero}')
        else:
            print(f'HAS ENCERTAT :D !!')
            break
    else:
        print("Introdueix un nombre entre 0 i 100 siusplau")