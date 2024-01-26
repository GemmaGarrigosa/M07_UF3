
import random
escollit = random.randint(1,100)
intents = 0


while True:
    numero = int(input('Introdueix un numero'))
    if escollit > numero:
        print(f'El nombre és més gran que {numero}')
    elif escollit < numero:
        print(f'El nombre és més petit que {numero}')
    else:
        print(f'HAS ENCERTAT :D !!')
        break
