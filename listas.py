#Crear lista de 500 notas (1,5)
#Mock

import random
notas = []
for i in range(5):
    nota = random.randint(1,5)

    #llenar una lista
    notas.append(nota)

#Manipulando listas con python

notas.insert(1,80) #insertar un elemento en la posicion 1, el numero 80
notas.remove(80) #remover el numero 80 de la lista
notas.pop(0) #remover el elemento en posición 0 lista
notas.sort() #ordenar la lista de menor a mayor
notas.sort(reverse=True) #ordenar la lista de mayor a menor
notas.clear() #limpiar la lista, eliminar todos los elementos
print(notas)
