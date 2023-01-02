#Tipo Float

a = 3.0
print(a)
#Para dar un formato F-STRING
print(f'{a:.2f}')
a = a/9
print(f'{a:.4f}')

#Constructor float
a = float(20)
print(a)

a = float('29')
print(a)

#notacion exponencial
a = 3e5
print(a)

a = 3e-6
print(f'a: {a:.6f}')

#cualquier calculo donde intervenga un FLOAT toodo se promueve a float
a = 6 + 0.4
print(a)
