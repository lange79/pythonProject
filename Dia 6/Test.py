from pathlib import Path
ruta_base=Path.home()
print(ruta_base)

from pathlib import Path

guia=Path("Curso Python","Día 6","practicas_path.py")
ruta=guia.relative_to(Path("Curso Python"))
print(ruta,guia)
