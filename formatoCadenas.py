#Dar formato a un string

nombre = "JUAN"
edad = 28
mensaje_formato = "Mi nombre es %s y tengo %d años"%(nombre, edad)
'''%s es parametro String %d es parametro entero %.2f es para flotantes'''
print(mensaje_formato)

persona = ('Karla', 'GOmez', 5000.00)
mensaje_formato = 'Hola %s %s Tu sueldo es %.2f'%persona
print(mensaje_formato)


#USO DE FORMAT
nombre = 'Roberto Carlos'
edad = 23
sueldo = 3500.456
mensaje_formato = 'Nombre: {} Edad: {} sueldo: {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_formato)

#OTRA FORMA CON POSICIONES
mensaje_formato = 'Sueldo: {2:.2f} Nombre: {0} Edad: {1} '.format(nombre, edad, sueldo)
print(mensaje_formato)

#OTRA FORMA
mensaje_formato = 'Nombre: {n} Edad: {e} Sueldo: {su:.2f}'.format(su=sueldo, e=edad, n=nombre)
print(mensaje_formato)

#CON DICCIONARIO
diccionario = {'nombre':'Ruben', 'apellido':'Reyes', 'edad':23, 'sueldo':34567.458}
mensaje_formato = 'Nombre: {persona[nombre]} Apellido: {persona[apellido]} Edad: {persona[edad]} Sueldo: {persona[sueldo]:.2f} '.format(persona=diccionario)
print(mensaje_formato)

#F-STRING
mensaje_formato = f'Nombre: {nombre}, Edad: {edad}'    #-------> se pueden poner hasta funciones

#print
print(nombre, edad, sueldo, sep=", ")