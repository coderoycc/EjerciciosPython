caracteres = b'Hola mundo'
print(caracteres)

mensaje = b'Universidad Python'
print(mensaje[-1])
print(chr(mensaje[-1]))


#Convirtiendo BYTE a STR e INVERSA
string = 'Programación python'
print(f'original \n\t{string}')
#String a Bytes
bytes = string.encode('UTF-8') #Se convierte a Bytes
print(f'convertido a bytes \n\t{bytes}')

#Bytes a STRING
string2 = bytes.decode('UTF-8')
print(f'Decodificado: \n\t{string2}')
print(f'Son iguales?: {string == string2}')