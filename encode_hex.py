import binascii
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'{self.nombre},{self.edad}\n'

#TEXTO
text = 'más comida perra\n'
otrav = text.encode('utf-8')
otrav = binascii.hexlify(otrav)
print('Original :', repr(text))
print('Codificado en Binario-hexadecimal: ', otrav, type(otrav))


#OBJETO CON LA AYUDA STR
p1 = Persona('Roberto', 23)
cadenaPer = p1.__str__().encode('utf-8')
cadenaPer = binascii.hexlify(cadenaPer)
print('Codificado: ', cadenaPer, type(cadenaPer))

p2 = Persona('Roberto Carlos Chambi Calizaya', 23)
nuevaCad = p2.__str__().encode('utf-8')
nuevaCad = binascii.hexlify(nuevaCad)

#ESCRIBIMOS EN EL ARCHIVO 'ab' Para sobrescribir
with open('binario.dat', 'ab') as archivo:
    #archivo.write(otrav)
    #archivo.write(cadenaPer)
    archivo.write(nuevaCad)

#LEEMOS DEL ARCHIVO
with open('binario.dat', 'rb') as arch:
    salida = binascii.unhexlify(arch.read())
    print(salida.decode('utf-8'))


