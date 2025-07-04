# LISTAS

mi_lista = ["a","b","c"] #lista 1
mi_lista2 = ["d","e","f"] #lista 2
mi_lista3 = mi_lista + mi_lista2 #concateno dos listas para crear una variable llamada lista 3 que concatena lista 1 + 2
print(type(mi_lista)) #imprime el tipo de variable llamada mi_lista
resultado_1 = mi_lista
print(resultado_1) #imprime la lista 1
resultado_2 = mi_lista + mi_lista2
print(resultado_2) # imprime la suja de lista 1 mas lista 2
resultado_3 = mi_lista3
print(resultado_3) #imprime la nueva lista 3
resultado_4 = mi_lista[0]
print(resultado_4) #impime el indice 0 de la lista
resultado_5 = mi_lista[0:2]
print(resultado_5) #imprime el indice 0 hasta el indice 2 sin incluir el 2
resultado_6 = mi_lista3[0::2]
print(resultado_6) #imprime todos los resultados de la lista 3 pero saltando de a 2 caracteres iniciando desde el indice 0