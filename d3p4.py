#PROPIEDADES DE STRING


# 1 INMUTABLIDAD
"""
nombre = "Carina"
nombre[0] ="K"
print(nombre)
""" # Al imprimir este codigo genera error por que los STRING son inmutabes

# Para solucionar lo anterior reordemos que las variables se pueden renombrar ejemplo

nombre = "Carina"
nombre = "Karina" #este reescribe la variable llamada nombre)
print(nombre)

# 2 CONCATENAR

n1 = "Kari"
n2 = "na"
print(n1+n2)

# 3 multiplicar

palabra = "hola"
print(palabra*3)

# 4 Varias lineas de codigo

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

# 5 booleano

print("agua" in poema) # esta preguntando si la palabra agua esta en la variable llamada poema
print("sol" in poema)
print("sol" not in poema)

# 6 len

print(len(poema))