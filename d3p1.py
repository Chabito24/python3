mi_texto = "Esto es una prueba"
resultado = mi_texto[2]
resultadoneg = mi_texto[-16]
print(resultado)
print(resultadoneg)


"""
se puede generar la visualizacion positiva o negativa  de la siguiente manera}

POSITIVA
Esto es una prueba
012345678911111111
          01234567
inicia desde 0 con la leta "E" y termina con 17 que es la ultima letra "a"

Esto es una prueba
------------------ menos
011111111987654321
 76543210
 
 en el ejemplo de arriba [2] y [-16] corresponden a la letra "t"
 es sensible a mayusculas
 si la letra no existe genera error

"""

#METODOS (index)

resultadometodo = mi_texto.index("e") #aqui usamos unicamente el Sub: str, el sub estring es en contrar ala ubicacion de una letra en la variable asignada
print(resultadometodo)

#Ejemplo 2

resultadometodo2 = mi_texto.index("e",7) #aqui buscamos nuevamente la letra "e" pero iniciando la busqueda desde el indice 7 en adelante de izquierda a derecha
print(resultadometodo2)

resultadometodo3 =mi_texto.index("e",1,6) #Error ya que solo busca desde el 1 hasta antes del 5


#METODOS (rindex)

resultadometodo = mi_texto.rindex("a") #busca de derecha a izquierda
print(resultadometodo)