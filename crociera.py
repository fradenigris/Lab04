from persona import Persona
from cabina import Cabina
from cabina_animali import CabinaAnimali
from cabina_deluxe import CabinaDeluxe

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO

        self._nome = nome
        self.cabine = list()
        self.persone = list()

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

        try:
            with open(file_path, encoding = 'utf-8', newline='') as file:
                for riga in file:
                    campi = riga.strip().split(',')
                    if len(campi) == 3:
                        persona = Persona(
                            codice = campi[0],
                            nome = campi[1],
                            cognome = campi[2]
                        )
                        self.persone.append(persona)

                    elif len(campi) == 4:
                        cabina = Cabina(
                            codice = campi[0],
                            numLetti = int(campi[1]),
                            ponte = int(campi[2]),
                            prezzo = float(campi[3])
                        )
                        self.cabine.append(cabina)

                    elif len(campi) == 5:
                        if campi[-1].isdigit():
                            cabina = CabinaAnimali(
                                codice = campi[0],
                                numLetti = int(campi[1]),
                                ponte = int(campi[2]),
                                prezzo = float(campi[3]) * (1 + (0.10 * float(campi[4]))),
                                numAnimali = int(campi[4])
                            )
                            self.cabine.append(cabina)

                        else:
                            cabina = CabinaDeluxe(
                                codice = campi[0],
                                numLetti = int(campi[1]),
                                ponte = int(campi[2]),
                                prezzo = float(campi[3]) * 1.20,
                                tipologia = campi[4]
                            )
                            self.cabine.append(cabina)

            return self.cabine, self.persone

        except FileNotFoundError:
            return None

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

