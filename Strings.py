#Profuindizando Strings

#concatenacion
variable = " De Bolivia"
mensaje = 'Hola ' 'Amigos'+variable
print(mensaje)

#AYUDA EN UNA CLASE o metodo
help(str.isalnum)
print((-34).__abs__())
print("".isalnum())

"""DOCSTING"""
'''
Si usas DocsString puedes verlo con help(clase.metodo)
o usando clase.__doc__  
clase.metodo.__doc__
'''

"""Los STR son inmutables con los metodos, solo mutan cuando se hace una nueva asignacion
    b = a.metodo() ----> a no cambia
    a = a.metodo() ----> a cambia
"""

#CADENAS JOIN
#En un iterable AÑADE UNA CADENA ENTRE LOS ELEMENTOS
it1 = ('Hola', 'Mundo')
it2 = ['Hola', 'De', 'nuevo']
it3 = 'UMSA'
it4 = {'nombre':'juan', 'apellido':'Perez', 'edad':'18'}
print(' '.join(it1))
print(' '.join(it2))
print('.'.join(it3))
print('-'.join(it4.keys()))
print('_'.join(it4.values()))

#SPLIT
cadena = "Hola Persona Como Estas         Desde Ayer"
print(cadena.split(' ', 2)) #MAX SPLIT