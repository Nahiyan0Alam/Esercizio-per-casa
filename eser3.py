from Esercizio_1 import Prodotto
from Esercizio_2 import Magazzino
import csv

class MagazzinoConSalvataggio(Magazzino):
    def salva_su_file(self, nome_file):
        with open(nome_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for prodotto in self.prodotti:
                writer.writerow([prodotto.get_nome(), prodotto.get_prezzo(), prodotto.get_quantita()])
        print(f"Inventario salvato su {nome_file}")

if __name__ == "__main__":
    magazzino = MagazzinoConSalvataggio()
    p1 = Prodotto(nome="Maglietta", prezzo=15.99, quantita=50)
    p2 = Prodotto(nome="Pantaloni", prezzo=29.99, quantita=30)
    magazzino.aggiungi_prodotto(p1)
    magazzino.aggiungi_prodotto(p2)
    magazzino.salva_su_file('inventario.csv')