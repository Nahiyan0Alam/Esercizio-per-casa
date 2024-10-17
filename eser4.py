import csv
from Esercizio_1 import Prodotto
from Esercizio_2 import Magazzino

class MagazzinoConVisualizza(Magazzino):
    def visualizza_magazzino(self, nome_file):
        try:
            with open(nome_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(f"Nome: {row[0]}, Prezzo: {row[1]}, Quantita: {row[2]}")
        except FileNotFoundError:
            print(f"Il file {nome_file} non esiste.")

if __name__ == "__main__":
    magazzino = MagazzinoConVisualizza()
    magazzino.visualizza_magazzino('inventario.csv')