import random
def main(text):
    clave = [random.randint(0,1) for _ in range(len(text))]
    enc = ""
    denc = ""
    for i in range(len(text)):
        enc += chr(ord(text[i]) ^ clave[i])
        denc += chr(ord(enc[i]) ^ clave[i])
    return enc, denc, clave
text = input("Ingresa una palabra: ")
enc, denc, clave = main(text)
print("Texto plano: ",text)
print("Clave: ",clave)
print("Encriptado: ",enc)
print("Desencriptado: ",denc)
