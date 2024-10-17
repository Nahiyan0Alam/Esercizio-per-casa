class Prodotto:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_quantita(self):
        return self.quantita

    def set_quantita(self, quantita):
        self.quantita = quantita

    def calcola_valore(self):
        return self.prezzo * self.quantita

    def aggiorna_quantita(self, nuova_quantita):
        self.quantita = nuova_quantita

    def toString(self):
        return "Nome: " + self.nome + ", Prezzo: " + str(self.prezzo) + ", Quantita: " + str(self.quantita) + ", Valore Totale: " + str(self.calcola_valore())

Prodotto1 = Prodotto("Laptop", 1320.50, 5)
print(Prodotto1.toString())

