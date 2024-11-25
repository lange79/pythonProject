texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra= "ayuda" in texto

print(palabra)

import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
patron= "hola"
busqueda=re.search(patron, texto)
print(busqueda)

patron= "ayuda"
busqueda=re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
busqueda=re.findall(patron, texto)
print(busqueda)
print(len(busqueda))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


texto = "Llama al 564-525-6588 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"
resultado = re.search(patron, texto)

print(resultado)
print(resultado.group())

patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)

print(resultado)
print(resultado.group())

patron = re.compile (r"(\d{3})-(\d{3})-(\d{4})")
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))

clave = input("clave: ")

patron = r"\D{1}\w{7}"

chequear = re.search(patron, clave)

print(chequear)


texto = "No atendemos los lunes por la tarde"

buscar = re.search(r"lunes|martes", texto)
print(buscar)

buscar = re.search(r"demos", texto)
print(buscar)

buscar = re.search(r"....demos...", texto)
print(buscar)


buscar = re.search(r"^\D", texto)
print(buscar)


buscar = re.search(r"\D$", texto)
print(buscar)

buscar = re.findall(r"[^\s]", texto)
print(buscar)

buscar = re.findall(r"[^\s]+", texto)
print(buscar)



import re

def verificar_email(email):
    email=email.lower()
    patron = r"\w+@\w+\.com(?:\.[a-z]{2})?$"
    valida= re.search(patron,email)
    if valida:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email("usuario@host.com.")

import re


def verificar_saludo(frase):
    frase=frase.lower()
    patron=r"^[hola]+\w"
    verifica=re.search(patron,frase)
    if verifica:
        print("Ok")
    else:
        print("No has saludado")

verificar_saludo("Hola. Necesito un favor")