from exercici32 import llista_quadrat
nums = input('Introdueix 10 nombres')
nums = nums.split(" ")
llista = [int(num) for num in nums]

llista_quadrat(llista)