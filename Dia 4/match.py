serie = "N-02"

"""if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe el producto")"""



"""match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe el producto")"""

cliente ={"Nombre":"Federico",
          "Edad":45,
          "Ocupacion":"instructor"}

pelicula = {"Titulo":"Matrix",
            "Ficha_tecnica":{"Protagonista":"keanu Reeves","Director":"Lana y Lilly Wachowski"}}

elementos = [cliente, pelicula,"Libro"]
for e in elementos:
    match e:
        case{"Nombre": nombre,
             "Edad": edad,
             "Ocupacion": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"Titulo":titulo,
              "Ficha_tecnica":{"Protagonista":protagonista,
                               "Director":director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto.")