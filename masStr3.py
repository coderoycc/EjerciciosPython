#Contamos las subcadenas que hay en una cadena
cadena = "cuando allá se pase lista, cuando allá se pase lista, cuando allá se pase lista a mi nombre yo feliz responderé"
print(cadena.count('e'))


#Convertimos las cadenas a mayusculas
cadena = cadena.upper()
print(cadena)

#Converti a minusculas una cadena
cadena = cadena.lower()
print(cadena)

#Startwith INICIA CON...
print(cadena.startswith('cuando'))

#endswith TERINA CON...
print(cadena.upper().endswith('É'))

#Preguntar si una cadena contiene unicamente caracteres en minuscula o mayuscula
print(cadena.islower())
print(cadena.isupper())

#alinear cadena a la izquierda
nueva = "Esta es una cadena de prueba"
print(nueva.ljust(50, '-'))

#alinear cadena a la derecha
print(nueva.rjust(50,'-'))

#centrar cadena
print(nueva.center(50, ' '))

#reemplazar contenido
print(nueva.replace(' ', '-'))

#Strip permite eliminar caracteres al inicio y final de una cadena
nueva = " +++ "+nueva+' +++ '
print(nueva)
print(nueva.strip())
print(nueva.strip(' +++ '))
print(nueva.lstrip(' +'))
print(nueva.rstrip(' +'))

#Desempaquetado
a, b, c = 1, 2, 3
print(a, b,c)
a, *b = 1, 2, 3, 4
print(a, b, type(b))

#PARTITION divide una cadena en 2 con un caracter en especial
cadena = '12:20'
hora, separador, minuto = cadena.partition(':')
print(hora, separador, minuto)