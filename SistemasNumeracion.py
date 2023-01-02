"""Produndizando el sistema decimas"""
#binario
a = 0b1010
print(f'a: {a}')

#Octal
a = 0o12
print(f'a: {a}')

#Hexadecimal
a = 0xa
print(f'a: {a}')



#Usando constructor de INT para sistemas numericos

#Convertir un tipo entero invcluyendo la base
a = int('23', 10)
print(f'decimal: {a}')
#Converir a binario
a = int('10111', 2)
print(f'binario {a}')
#Base octal
a = int('27', 8)
print(f'octal: {a}')
#Base 16
a = int('17', 16)
print(f'Hexadecimal: {a}')

a = 16
print(hex(a))
print(bin(a))

