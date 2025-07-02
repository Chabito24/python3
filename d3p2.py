#slicing permite estraer parte de una cadena de texto para almacenarlo en otr avariable

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:5] #no es inclusivo toma desde el indice 2 hasta el 4 sin incluir el 5
print(fragmento)

fragmento2 = texto[2:10:2]#toma desde el hcaracter 10 sin incluir el 10 saltando dos caracteres
print(fragmento2)

fragmento3 = texto[::2] #toma desde el primer hasta el ultimo indice y salta de a 2 caracteres
print(fragmento3)

fragmento4 = texto[::-1] #toma toda la cadena del string peor la revez
print(fragmento4)