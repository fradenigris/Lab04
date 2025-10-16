from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo, numAnimali):
        super().__init__(codice, numLetti, ponte, prezzo)
        self.numAnimali = numAnimali

    def __str__(self):
        info_base = super().__str__()
        return f"{info_base}, Numero di animali consentito: {self.numAnimali}"