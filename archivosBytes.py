
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'{self.nombre} {self.edad}\n'



p1 = Persona('Roberto', 23)
p2 = Persona('Ramiro', 21)

with open('datos.dat', "wb") as archivo:
    archivo.write(p1.__str__().encode('utf-8'))
    archivo.write(p2.__str__().encode('utf-8'))

with open('datos.dat', 'rb') as arch:
    for linea in arch:
        print(linea)
