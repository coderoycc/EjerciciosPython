#BOoleano

#Con tipos Numericos FALSE --> 0, TRUE --> 1
valor = 0
resultado = bool(valor)
print(valor, resultado)

valor = 1
resultado = bool(valor)
print(valor, resultado)

valor = 10.1
resultado = bool(valor)
print(valor, resultado)

valor = 21
resultado = bool(valor)
print(valor, resultado)


#Con tipos String FALSE --> '', TRUE --> 'Cualquier cadena'
valor = ''
resultado = bool(valor)
print(valor, resultado)

valor = 'estrue'
resultado = bool(valor)
print(valor, resultado)

valor = ' '
resultado = bool(valor)
print(valor, resultado)


#COLECCIONES    FALSE --> colecciones vacias
#               TRUE --> colecciones con valores
valor = []
resultado = bool(valor)
print(valor, resultado)

valor = [1, 4]
resultado = bool(valor)
print(valor, resultado)

valor = ['']
resultado = bool(valor)
print(valor, resultado)

#TUPLA
valor = ()
resultado = bool(valor)
print(valor, resultado)

valor = (1,)
resultado = bool(valor)
print(valor, resultado)

#Diccionario
valor = {}
resultado = bool(valor)
print(valor, resultado)

valor = {1:'Uno', 2:'Dos',3:'Tres'}
resultado = bool(valor)
print(valor, resultado)


#EN SENTENCIAS DE CONTROL
valor=(1,)
#Convierte automaticamente a tipo bool en sentencias de control
if valor:
    print('Tiene elementos')
else:
    print('No tiene elementos')
