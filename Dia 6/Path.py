from pathlib import Path

base=Path.home()
guia=Path("Barcelona", "Sagrada_familia.txt")
print(guia)

guia=Path(base,"Barcelona", "Sagrada_familia.txt")
print(base)
print(guia)

base=Path.home()
guia=Path(base,"Europa", "España",Path("Barcelona", "Sagrada_familia.txt"))
guia2=guia.with_name("La_Pedrera.txt")

print(guia)
print(guia.parent)
print(guia.parent.parent)

print(guia2)

guia3= Path(Path.home(),"Europa")
for txt in Path(guia3).glob("*.txt"):
    print(txt)

guia3= Path(Path.home(),"Europa")
for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

guia4=Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa=guia4.relative_to(Path("Europa"))
en_espania=guia4.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)
