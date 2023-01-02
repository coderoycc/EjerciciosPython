import math
from decimal import Decimal
####        FLOAT
infinito = float('inf') #POSITIVO
print(infinito)
#Preguntamos si es infinito
print(f'Es infinito?: {math.isinf(infinito)}')

infinito_nega = float('-inf')
print(infinito_nega)
print(f'Es infinito?: {math.isinf(infinito_nega)}')


######     MATH
infinito = math.inf
print(infinito)
print(f'Es infinito: {math.isinf(infinito)}')

infinito_nega = -math.inf
print(infinito_nega)
print(f'Es infinito: {math.isinf(infinito_nega)}')


#####     DECIMAL
infinito = Decimal('Infinity')
print(infinito)
print(f'Es infinito: {math.isinf(infinito)}')


infinito_nega = Decimal('-Infinity')
print(infinito_nega)
print(f'Es infinito: {math.isinf(infinito_nega)}')