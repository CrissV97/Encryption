import random
def main(text):
    clave = [random.randint(0,1) for _ in range(len(text))]
    #for i in range(len(text)):
    enc += "".join([chr(ord(c) ^ k) for c, k in zip(text, clave)])
    denc += "".join([chr(ord(c) ^ k) for c, k in zip(enc, clave)])
    return enc, denc, clave
text = input("Ingresa una palabra: ")
enc, denc, clave = main(text)
print(f"Texto original: {text}")
print(f"Clave: {clave}")
print(f"Codificado: {enc}")
print(f"Decodificado: {denc}")