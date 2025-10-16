class Cabina:
    def __init__(self, codice, numLetti, ponte, prezzo):
        self.codice = codice
        self.numLetti = numLetti
        self.ponte = ponte
        self.prezzo = prezzo

    def __str__(self):
        return f"Cabina {self.codice} - Ponte: {self.ponte}, Letti: {self.numLetti}, Prezzo: {self.prezzo}€"

    def __repr__(self):
        return f"Cabina(codice = '{self.codice}', numLetti = {self.numLetti}, ponte = {self.ponte}, prezzo = {self.prezzo})"