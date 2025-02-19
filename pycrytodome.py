# Instalar librería pycryptodome
# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
# Generar clave y vector de inicialización (IV)
clave = get_random_bytes(16)
cipher = AES.new(clave, AES.MODE_EAX)

texto = input("\nEscribe un texto que quieras cifrar: ")
#Crea la carpeta si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")

# Cifrar mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")
cifrado, tag = cipher.encrypt_and_digest(mensaje)

print("Texto Cifrado:", cifrado)

#Guardar en archivo texto cifrado
with open("archivos/cifrado.txt", "wb") as file:
    file.write(cifrado)
# Descifrar mensaje
cipher_dec = AES.new(clave, AES.MODE_EAX, cipher.nonce)
mensaje_descifrado = cipher_dec.decrypt(cifrado).decode()
print("Texto Descifrado:", mensaje_descifrado)
#Guardar en archivo texto descifrado
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)