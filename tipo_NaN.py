import math
from decimal import Decimal
a = float('NaN')
#Not a Number
#Tipo de dato numerico para identificar un numero no definido
print(a)
print(f'Es NaN: {math.isnan(a)}')

a = Decimal('Nan')
print(a)
print(f'Es Nan: {math.isnan(a)}') 