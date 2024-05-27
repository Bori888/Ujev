import Ujev
import random
def lista():
    koszontesek = []
    f = open("ujev.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(len(sorok)):
        koszontes = Ujev.Ujev(sorok[i])
        koszontesek.append(koszontes)
    return koszontesek

def veletlen(lista: list[Ujev.Ujev]):
    kevdes_lista = []
    for i in range(len(lista)):
        if "kedves" == lista[i].kategoria:
            kevdes_lista.append(lista[i].szoveg)
    print(f"38.\n\t{random.choice(kevdes_lista)}")