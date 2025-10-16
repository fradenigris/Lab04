from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo, tipologia):
        super().__init__(codice, numLetti, ponte, prezzo)
        self.tipologia = tipologia

    def __str__(self):
        info_base = super().__str__()
        return f"{info_base}, Tipologia: Deluxe ({self.tipologia})"