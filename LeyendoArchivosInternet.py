# Leer contenido online
from urllib.request import urlopen

with urlopen('http://roy281inf.rf.gd/docs/datos.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

#escribimos el contenido en un nuevo archivo
with open('documento.html', 'w', encoding='utf-8') as archivo:
    archivo.write(contenido)