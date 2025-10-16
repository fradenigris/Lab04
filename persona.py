class Persona:
    def __init__(self, nome, cognome, codice):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.nome} {self.cognome} (ID: {self.codice})"

    def __repr__(self):
        return f"Persona(codice = '{self.codice}', nome = '{self.nome}', cognome = '{self.cognome}')"