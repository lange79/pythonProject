import bs4
import requests


resultado =requests.get("https://www.escueladirecta.com/courses")

#print(type(resultado))
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

#print(sopa.select("title"))

#print(sopa.select("p"))
#print(len(sopa.select("p")))
#print(sopa.select("h1"))

#print(sopa.select("title")[0])
#print(sopa.select("title")[0].getText())

#parrafo_especial = sopa.select("p")[3].getText()
#print(parrafo_especial)


imagenes = sopa.select(".course-box-image")
for i in imagenes:
    print(i)

imagenes = sopa.select(".course-box-image")[0]["src"]
print(imagenes)

imagen_curso_1 = requests.get(imagenes)
#print(imagen_curso_1.content)

f = open("mi_imagen.jpg", "wb")
f.write(imagen_curso_1.content)
f.close()
