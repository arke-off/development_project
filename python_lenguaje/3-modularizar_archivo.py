import os
##importa el ascii
ruta_archivo = "C:/Users/santi/OneDrive/Documentos/GitHub/phython_lenguaje/python_lenguaje/resources/ascii.txt"  # Ejemplo de ruta
archivo = open(ruta_archivo, "r")
contenido_ascii = archivo.read()
print(contenido_ascii)
archivo.close()

