class Ujev:
    def __init__(self, sor: str):
        adatok = sor.strip().split(";")
        self.kategoria = adatok[0]
        self.szoveg = adatok[1]
