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
                categorieDisponibili = list(magazzino.keys())
                
                os.system("cls")
                categoria = funzioni.chiediCategoria(categorieDisponibili)
                    
                prodottiDisponibili = magazzino[categoria].keys()
                
                os.system("cls")
                prodotto = funzioni.chiediProdotto(categoria, prodottiDisponibili)
                    
                qtaProdotto = magazzino[categoria].get(prodotto)
                    
                os.system("cls")
                print(f"Quantità dell'articolo '{prodotto}': {qtaProdotto}")
                
                qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
                
                while not qtaNuova.isnumeric():
                    print("Devi inserire un numero valido intero!")
                    qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
                
                qtaNuova = int(qtaNuova)
                
                funzioni.modificaQta(magazzino, categoria, prodotto, qtaNuova)

                print("\nQuantità aggiornata con successo!")

                funzioni.salvaMagazzino(magazzino)
                os.system("pause")
            case "2":
                os.system("cls")
                
                print("Opzioni:")
                print("[1] Aggiungi un prodotto")
                print("[2] Rimuovi un prodotto")
                aggiungiRimuovi = input("\nScegli un'opzione: ")
                
                while aggiungiRimuovi != "1" and aggiungiRimuovi != "2":
                    print("Devi inserire un'opzione valida!")
                    aggiungiRimuovi = input("\nScegli un'opzione: ")
                    
                categorieDisponibili = list(magazzino.keys())
                
                os.system("cls")
                categoria = funzioni.chiediCategoria(categorieDisponibili)
                    
                if aggiungiRimuovi == "1":
                    prodotto = input("\nInserisci il nome del prodotto: ").lower().capitalize()
                    
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
                    prodotto = funzioni.chiediProdotto(categoria, prodottiDisponibili)
                    
                    magazzino = funzioni.rimuoviArticolo(magazzino, categoria, prodotto)
                    print("\nProdotto rimosso con successo!")
                    
                funzioni.salvaMagazzino(magazzino)
                os.system("pause")
            case "3":
                categorieDisponibili = list(magazzino.keys())
                
                os.system("cls")
                categoria = funzioni.chiediCategoria(categorieDisponibili)
                
                articoliCategoria = funzioni.stampaArticoliCategoria(magazzino, categoria)

                os.system("cls")

                print(f"Prodotti nella categoria '{categoria}':\n")
                print(articoliCategoria)
                
                funzioni.salvaMagazzino(magazzino)
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
                    categorieEsistenti = list(magazzino.keys())
                    
                    categoria = input("Inserisci la categoria da aggiungere: ")

                    while categorieEsistenti.__contains__(categoria):
                        print("Devi inserire una categoria non già esistente!")
                        categoria = input("Inserisci la categoria da aggiungere: ")
                    
                    magazzino = funzioni.aggiungiCategoria(magazzino, categoria)
                    print("\nCategoria aggiunta con successo!")
                else:
                    categorieDisponibili = list(magazzino.keys())
                    
                    categoria = funzioni.chiediCategoria(categorieDisponibili)
                    
                    magazzino = funzioni.rimuoviCategoria(magazzino, categoria)
                    print("\nCategoria rimossa con successo!")
                
                funzioni.salvaMagazzino(magazzino)
                os.system("pause")
            case "5":
                funzioni.salvaMagazzino(magazzino)
                funzioni.salvaMagazzinoTxt(magazzino)

                os.system("cls")
                print("Magazzino salvato correttamente nel file magazzino.txt!")
                os.system("pause")
            case "0":
                esci = True
                funzioni.esci()

if __name__ == "__main__":
    main()