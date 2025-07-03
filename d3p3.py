#METODOS de String

"""
upper() - pasar a mayúsculas
lower() - pasar a úsculas
split() - separar en partes (lista)
join() - unir items usando separador
find() - encontrar un sb-string
replace() - reemplaza un substring

"""

#upper

texto1 = "este es un texto"
metodo1 = texto1.upper() # cambia todo el texto de la variable a mayúscula
metodo2 = texto1[5::1].upper() # le incluyo un indice de inicio 5 de fin en blanco para que tome el restante del texto y cada cuantos caracteres debe cambiar que seria el 1 para que no haga saltos
print(metodo1)
print(metodo2)

#lower

texto2 = "ESTE ES UN TEXTO"
metodo3 = texto2.lower()
metodo4 = texto2[1::1].lower()
print(metodo3)
print(metodo4)

#split

metodo5 = texto1.split() #separa palabra por palabra del texto
metodo6 = texto1.split("t") #separa con el criterio de separacion cada que exista una letra "t"
metodo7 = texto1[5::1].split()#se aplica indica inicio finalizacion y cada cuantos caracteres
print(metodo5)
print(metodo6)
print(metodo7)

#join

texto3 = "aprender"
texto4 = "python"
texto5 = "es"
texto6 = "genial"
e = " ".join([texto3,texto4,texto5,texto6])
print(e)


#find

metodo8 = texto1.find("s") #similar a index pero no genera error cuando no existe el caracter en la busqueda
print(metodo8)


#replace

metodo9 = texto1.replace("texto","parrafo") #reemplaza una palabra
print(metodo9)
metodo10 = texto1.replace("e","a") #reemplaza una letra en todo el texto
print(metodo10)