from Esercizio_1 import Prodotto
class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def rimuovi_prodotto(self, nome_prodotto):
        for prodotto in self.prodotti:
            if prodotto.get_nome() == nome_prodotto:
                self.prodotti.remove(prodotto)
                return
        print(f"Prodotto '{nome_prodotto}' non trovato nel magazzino.")

    def valore_totale(self):
        valore = 0
        for prodotto in self.prodotti:
            valore += prodotto.calcola_valore()
        return valore


magazzino = Magazzino()
p1 = Prodotto(nome="Maglietta", prezzo=15.99, quantita=50)
p2 = Prodotto(nome="Pantaloni", prezzo=29.99, quantita=30)
magazzino.aggiungi_prodotto(p1)
magazzino.aggiungi_prodotto(p2)
print(magazzino.valore_totale())
magazzino.rimuovi_prodotto("Maglietta")
print(magazzino.valore_totale())
