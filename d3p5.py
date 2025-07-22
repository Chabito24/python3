# LISTAS

mi_lista = ["a","b","c"] #lista 1
mi_lista2 = ["d","e","f"] #lista 2
mi_lista3 = mi_lista + mi_lista2 #concateno dos listas para crear una variable llamada lista 3 que concatena lista 1 + 2
print(type(mi_lista)) #imprime el tipo de variable llamada mi_lista
resultado = len(mi_lista) #muestra el largo de la lista
print(resultado)

resultado_1 = mi_lista
print(resultado_1) #imprime la lista 1

resultado_2 = mi_lista + mi_lista2
print(resultado_2) # imprime la suma de datos de la lista 1 mas lista 2

resultado_3 = mi_lista3
print(resultado_3) #imprime la nueva lista 3

resultado_4 = mi_lista[0]
print(resultado_4) #impime el indice 0 de la lista

resultado_5 = mi_lista[0:2]
print(resultado_5) #imprime el indice 0 hasta el indice 2 sin incluir el 2

resultado_6 = mi_lista3[0::2]
print(resultado_6) #imprime todos los resultados de la lista 3 pero saltando de a 2 caracteres iniciando desde el indice 0

mi_lista3[0] = "alfa"
print(mi_lista3) #cambio el valor de es indice 0 de "a" por "alfa"

mi_lista3.append("g")
print(mi_lista3) #agregamos un elemento a la lista

mi_lista3.pop() #si se deja sin datos entre los parentesis significa que se eliminara el ultimo de sus elementos, de lo contrario debo indocar el indice que se va a eliminar
print(mi_lista3)

eliminado = mi_lista3.pop(0) #guasrda el elemento eliminado en una variable
print(mi_lista3)
print("elemento eliminado " + "\""+ eliminado + "\"")

#METODOS MAS IMPORTANTES

listanew = ["g","o","b","m","c"]
print(listanew)

#ordenar
listanew.sort() #ordena los elementos de la la lista
print(listanew)

nuevalista = listanew.sort()
print(nuevalista)
print(type(nuevalista)) #Solo ordena no permite retornar ese valor lo vemos generando el RUN nos dice que esto no es ningun tipo de dato o de clase solo permite organoizar, es un objeto que no tiene un valor, no confundir al no tener un valor no sognifica que le de valor cero, simplemente tiene ausencia de cualquier tipo de valor

listanew.reverse()
print(listanew) #los asigna en orden inverso  

