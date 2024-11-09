def lee_recetas(ruta):
    categorias=[]
    cant=0
    for item in ruta.iterdir():
        if item.is_dir():
            categorias.append(item.name)
    print("Elija el Numero de alguna de las categorias:")
    opcion = -1
    while opcion < 1 or opcion > cant+1:
        for categoria in categorias:
            cant += 1
            print(f"{[cant]} - {categoria}")
        print(f"{[cant+1]} - SALIR")

        opcion=int(input())


        if opcion < 1 or opcion > cant+1:
            system('cls')
            print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
            cant = 0
        else:
            cat_selecionada=categorias[opcion-1]
            ruta_categoria_selec=Path(ruta, cat_selecionada)
            recetas=[]
            for r in ruta_categoria_selec.iterdir():
                if r.is_file():
                    recetas.append(r.name)
            system('cls')
            print("Seleccion el numero correspondiente a la receta que desea leer:")
            opcion = -1
            cant=0
            while opcion < 1 or opcion > cant+1:
                for receta in recetas:
                    cant += 1
                    print(f"{[cant]} - {receta}")
                print(f"{[cant + 1]} - SALIR")
                opcion = int(input())
                input()
                if opcion < 1 or opcion > cant+1:
                    system('cls')
                    print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
                    cant = 0
                elif opcion==cant+1:
                    print("Opcion=Cantidad")
                    break
                else:
                    rec_selecionada = recetas[opcion - 1]
                    archivo=open(Path(ruta_categoria_selec, rec_selecionada))
                    print(archivo.read())
                    archivo.close()




def crea_recetas(ruta):
    categorias=[]
    cant=0
    for item in ruta.iterdir():
        if item.is_dir():
            categorias.append(item.name)
    print("Elija el Numero de la categorias donde desea crear una nueva receta:")
    opcion = 0
    while opcion < 1 or opcion > cant:
        for categoria in categorias:
            cant += 1
            print(f"{[cant]} - {categoria}")
        opcion=int(input())
        if opcion < 1 or opcion > cant:
            print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
            cant = 0
        else:
            cat_selecionada=categorias[opcion-1]
            ruta_categoria_selec=Path(ruta, cat_selecionada)
            nombre_receta=input("Ingrese el nombre de la nueva receta:")
            path=Path(ruta_categoria_selec,nombre_receta+".txt")
            print("ingrese la receta, y presione ENTER al finalizar")
            archivo = open(path,'w')
            archivo.write(input())
            archivo.close()


    
def crea_categoria(ruta):
    categorias = []
    cant = 0
    for item in ruta.iterdir():
        if item.is_dir():
            categorias.append(item.name)
    print("Estas son las categorias existentes:")
    for categoria in categorias:
        cant += 1
        print(f"{[cant]} - {categoria}")

    nombre_carpeta=input("Ingresa el nombre de la categoria de recetas que quieres agregar:")
    ruta_completa=Path(ruta,nombre_carpeta)
    ruta_completa.mkdir(parents=True, exist_ok=False)
    print(f"La categoria {nombre_carpeta} fue creada exitosamente {ruta_completa}")


def borra_recetas(ruta):
    categorias = []
    cant = 0
    for item in ruta.iterdir():
        if item.is_dir():
            categorias.append(item.name)
    print("Elija el Numero de las categoria donde esta la receta que quieres borrar:")
    opcion = 0
    while opcion < 1 or opcion > cant:
        for categoria in categorias:
            cant += 1
            print(f"{[cant]} - {categoria}")

        opcion = int(input())
        if opcion < 1 or opcion > cant:
            print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
            cant = 0
        else:
            cat_selecionada = categorias[opcion - 1]
            ruta_categoria_selec = Path(ruta, cat_selecionada)

            recetas = []
            for r in ruta_categoria_selec.iterdir():
                if r.is_file():
                    recetas.append(r.name)
            print("Seleccion el numero correspondiente a la receta que desea eliminar:")
            opcion = 0
            cant = 0
            while opcion < 1 or opcion > cant:
                for receta in recetas:
                    cant += 1
                    print(f"{[cant]} - {receta}")
                opcion = int(input())
                if opcion < 1 or opcion > cant:
                    print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
                    cant = 0
                else:
                    rec_selecionada = recetas[opcion - 1]
                    #archivo = open(Path(ruta_categoria_selec, rec_selecionada))
                    archivo = Path(ruta_categoria_selec, rec_selecionada)
                    if archivo.is_file():
                        archivo.unlink()
                        print(f"La receta: '{rec_selecionada}' se ha eliminado exitosamente de '{ruta_categoria_selec}'.")
                    else:
                        print(f"La receta: '{rec_selecionada}' no existe en la ruta especificada.")



def borra_categoria(ruta):

    categorias = []
    cant = 0
    for item in ruta.iterdir():
        if item.is_dir():
            categorias.append(item.name)
    print("Estas son las categorias existentes:")
    opcion = 0
    while opcion < 1 or opcion > cant:
        for categoria in categorias:
            cant += 1
            print(f"{[cant]} - {categoria}")
        print("Elija el Numero de las categoria que quiera borrar:")
        opcion = int(input())
        if opcion < 1 or opcion > cant:
            print("Seleccion invalidad, vuelva a seleccionar el numero de la opcion deseada:")
            cant = 0
        else:
            cat_selecionada = categorias[opcion - 1]
            ruta_categoria_selec = Path(ruta, cat_selecionada)

    ruta_categoria_selec.rmdir()
    print(f"La categoria {cat_selecionada} fue creada exitosamente {ruta_categoria_selec}")


from pathlib import Path
from os import system
cant_recetas=0
menu=0
print("""***************************************
*   Bienvenido Al Programa Recetario  *
***************************************   """)
dir_base=Path.home()
ruta_recetario=Path(dir_base,"Recetas")
for txt in Path(ruta_recetario).glob("**/*.txt"):
    cant_recetas+=1
print("La ruta de acceso al directorio de recetas es:\n", ruta_recetario)
print("La cantidad de Recetas es: ", cant_recetas)


while menu!=6:
    while menu<1 or menu>6:
        print("""*****************************************************
*          Menu De Opciones de Recetas              *
*                                                   *
*    1 - Para Seleccionar La Categoria De Recetas   *
*        A Leer.                                    *
*    2 - Para Crear Una Nueva Receta.               *
*    3 - Para Crear Una Nueva Categoria De Recetas. *
*    4 - Para Seleccionar La Categoria De Recetas   *
*        A Borrar.                                  *
*    5 - Para Borrar Una Categoria De Recetas.      *
*    6 - Finalizar El Programa.                     *
*****************************************************   
        """)
        menu=int(input("Seleccion la opcion deseada:"))
        if menu<1 or menu>6:
            print("Selecion invalidad, debe elegir una opcion del 1 al 6")
            pass
    match menu:
        case 1:
            system('cls')
            print("Vamos a leer una Receta:")
            lee_recetas(ruta_recetario)
        case 2:
            system('cls')
            print("Vamos a crear una Receta:")
            crea_recetas(ruta_recetario)
        case 3:
            system('cls')
            print("Vamos a crear una categoria de Recetas:")
            crea_categoria(ruta_recetario)
        case 4:
            system('cls')
            print("Vamos a borrar una Receta:")
            borra_recetas(ruta_recetario)
        case 5:
            system('cls')
            print("Vamos a borrar una categoria de Recetas:")
            borra_categoria(ruta_recetario)
        case _:
            system('cls')
            print("Programa finalizado.")









