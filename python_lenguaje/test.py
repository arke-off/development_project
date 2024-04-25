import os
import time
##1
x = input("Please enter hello: ")
##2
if (x=="hello"):
##3
    os.system('clear')
    ruta_archivo = "C:/Users/santi/OneDrive/Documentos/GitHub/phython_lenguaje/python_lenguaje/resources/ascii.txt"  # Ejemplo de ruta
    archivo = open(ruta_archivo, "r")
    contenido_ascii = archivo.read()
    print(contenido_ascii)
    archivo.close()
time.sleep(0.7)
print ("Welcome to the internet")