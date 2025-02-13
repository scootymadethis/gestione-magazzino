import funzioni
import os

def main():
    magazzino = funzioni.prendiMagazzino()
    
    esci = False

    while not esci:
        os.system("cls")
        funzioni.stampaMenu()

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                categorieDisponibli = magazzino.keys()
                
                os.system("cls")
                print("Categorie disponibili:")
                
                for k in categorieDisponibli:
                    print(k)
                
                categoria = input("\nInserisci il nome della categoria da modificare: ")
                
                while not categorieDisponibli.__contains__(categoria):
                    print("Devi inserire una categoria valida!")
                    categoria = input("\nInserisci il nome della categoria da modificare: ")
                    
                prodottiDisponibili = magazzino[categoria].keys()
                
                os.system("cls")
                print(f"Prodotti disponibili nella categoria '{categoria}':")
                
                for k in prodottiDisponibili:
                    print(k)
                    
                prodotto = input("\nInserisci il nome del prodotto da modificare: ")
                
                while not prodottiDisponibili.__contains__(prodotto):
                    print("Devi inserire un prodotto valido!")
                    prodotto = input("\nInserisci il nome del prodotto da modificare: ")
                    
                qtaProdotto = magazzino[categoria].get(prodotto)
                    
                os.system("cls")
                print(f"Quantità dell'articolo '{prodotto}': {qtaProdotto}")
                
                qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
                
                while not qtaNuova.isnumeric():
                    print("Devi inserire un numero valido intero!")
                    qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
                
                qtaNuova = int(qtaNuova)
                
                funzioni.modificaQta(magazzino, categoria, prodotto, qtaNuova)
            case "2":
                os.system("cls")
                
                print("Opzioni:")
                print("[1] Aggiungi un prodotto")
                print("[2] Rimuovi un prodotto")
                aggiungiRimuovi = input("\nScegli un'opzione: ")
                
                while aggiungiRimuovi != "1" and aggiungiRimuovi != "2":
                    print("Devi inserire un'opzione valida!")
                    aggiungiRimuovi = input("\nScegli un'opzione: ")
                    
                categorieDisponibli = magazzino.keys()
                
                os.system("cls")
                print("Categorie disponibili:")
                
                for k in categorieDisponibli:
                    print(k)
                
                categoria = input("\nInserisci il nome della categoria: ")
                
                while not categorieDisponibli.__contains__(categoria):
                    print("Devi inserire una categoria valida!")
                    categoria = input("\nInserisci il nome della categoria: ")
                    
                if aggiungiRimuovi == "1":
                    prodotto = input("\nInserisci il nome del prodotto: ")
                    
                    qtaProdotto = input("\nInserisci la quantità del nuovo prodotto: ")
                    
                    while not qtaProdotto.isnumeric():
                        print("Devi inserire un numero valido intero!")
                        qtaProdotto = input("\nInserisci la nuova quantità del prodotto: ")
                
                    qtaProdotto = int(qtaProdotto)
                    
                    magazzino = funzioni.aggiungiArticolo(magazzino, categoria, prodotto, qtaProdotto)
                    print("\nProdotto aggiunto con successo!")
                else:
                    prodottiDisponibili = magazzino[categoria].keys()
                    
                    os.system("cls")
                    print(f"Prodotti disponibili nella categoria '{categoria}':")
                    
                    for k in prodottiDisponibili:
                        print(k)
                        
                    prodotto = input("\nInserisci il nome del prodotto da rimuovere: ")
                    
                    while not prodottiDisponibili.__contains__(prodotto):
                        print("Devi inserire un prodotto valido!")
                        prodotto = input("\nInserisci il nome del prodotto da rimuovere: ")
                    
                    magazzino = funzioni.rimuoviArticolo(magazzino, categoria, prodotto)
                    print("\nProdotto rimosso con successo!")
                    
                os.system("pause")
            case "3":
                categorieDisponibli = magazzino.keys()
                
                os.system("cls")
                print("Categorie disponibili:")
                
                for k in categorieDisponibli:
                    print(k)
                
                categoria = input("\nInserisci il nome della categoria: ")
                
                while not categorieDisponibli.__contains__(categoria):
                    print("Devi inserire una categoria valida!")
                    categoria = input("\nInserisci il nome della categoria: ")
                
                articoliCategoria = funzioni.stampaArticoliCategoria(magazzino, categoria)

                os.system("cls")

                print(f"Prodotti nella categoria '{categoria}':\n")
                print(articoliCategoria)
                
                os.system("pause")
            case "4":
                os.system("cls")
                
                print("Opzioni:")
                print("[1] Aggiungi una categoria")
                print("[2] Rimuovi una categoria")
                aggiungiRimuovi = input("\nScegli un'opzione: ")
                
                while aggiungiRimuovi != "1" and aggiungiRimuovi != "2":
                    print("Devi inserire un'opzione valida!")
                    aggiungiRimuovi = input("\nScegli un'opzione: ")
                    
                if aggiungiRimuovi == "1":
                    categorieEsistenti = magazzino.keys()
                    
                    os.system("cls")
                    print("Categorie esistenti:")
                    
                    for k in categorieEsistenti:
                        print(k)
                    
                    categoria = input("\nInserisci il nome della categoria: ")
                    
                    while categorieEsistenti.__contains__(categoria):
                        print("Devi inserire una categoria non già esistente!")
                        categoria = input("\nInserisci il nome della categoria: ")
                    
                    magazzino = funzioni.aggiungiCategoria(magazzino, categoria)
                    print("\nCategoria aggiunta con successo!")
                else:
                    categorieDisponibli = magazzino.keys()
                    
                    os.system("cls")
                    print("Categorie disponibili:")
                    
                    for k in categorieDisponibli:
                        print(k)
                        
                    categoria = input("\nInserisci il nome della categoria: ")
                    
                    while not categorieDisponibli.__contains__(categoria):
                        print("Devi inserire una categoria valida!")
                        categoria = input("\nInserisci il nome della categoria: ")
                    
                    magazzino = funzioni.rimuoviCategoria(magazzino, categoria)
                    print("\nCategoria rimossa con successo!")
                
                os.system("pause")
            case "5":
                funzioni.salvaInfoMagazzino()
            case "0":
                esci = True
                funzioni.esci()

if __name__ == "__main__":
    main()