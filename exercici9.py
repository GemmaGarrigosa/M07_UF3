paraules = input("Introdueix dues paraules")

paraules = paraules.split()

paraula1 = paraules[1][:2] + paraules[0][2:]
paraula2 = paraules[0][:2] + paraules[1][2:]

print(f"{paraula1} {paraula2}")