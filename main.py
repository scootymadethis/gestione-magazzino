import funzioni
import os

def cls():
    os.system("cls")

def pause():
    os.system("pause")

def main():
    magazzino = funzioni.prendiMagazzino()
    
    esci = False

    while not esci:
        cls()
        funzioni.stampaMenu()

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                cls()

                categorieDisponibili = list(magazzino.keys())
                categoria = funzioni.chiediCategoria(categorieDisponibili)
                
                cls()
                prodottiDisponibili = list(magazzino[categoria].keys())
                prodotto = funzioni.chiediProdotto(categoria, prodottiDisponibili)
                
                qtaNuova = funzioni.chiediQta(magazzino, categoria, prodotto)
                
                funzioni.modificaQta(magazzino, categoria, prodotto, qtaNuova)

                print("\nQuantità aggiornata con successo!")

                funzioni.salvaMagazzino(magazzino)
                pause()
            case "2":
                cls()
                
                print("Opzioni:")
                print("[1] Aggiungi un prodotto")
                print("[2] Rimuovi un prodotto")
                aggiungiRimuovi = input("\nScegli un'opzione: ")
                
                while aggiungiRimuovi != "1" and aggiungiRimuovi != "2":
                    print("Devi inserire un'opzione valida!")
                    aggiungiRimuovi = input("\nScegli un'opzione: ")
                    
                categorieDisponibili = list(magazzino.keys())
                
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
                    
                    prodotto = funzioni.chiediProdotto(categoria, prodottiDisponibili)
                    
                    magazzino = funzioni.rimuoviArticolo(magazzino, categoria, prodotto)
                    print("\nProdotto rimosso con successo!")
                    
                funzioni.salvaMagazzino(magazzino)
                pause()
            case "3":
                cls()

                categorieDisponibili = list(magazzino.keys())
                
                categoria = funzioni.chiediCategoria(categorieDisponibili)
                
                articoliCategoria = funzioni.stampaArticoliCategoria(magazzino, categoria)

                print(f"Prodotti nella categoria '{categoria}':\n")
                print(articoliCategoria)
                
                funzioni.salvaMagazzino(magazzino)
                pause()
            case "4":
                cls()
                
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

                    while funzioni.categoriaEsiste(categorieEsistenti, categoria):
                        print("Devi inserire una categoria non già esistente!")
                    
                    magazzino = funzioni.aggiungiCategoria(magazzino, categoria)
                    print("\nCategoria aggiunta con successo!")
                else:
                    categorieDisponibili = list(magazzino.keys())
                    
                    categoria = funzioni.chiediCategoria(categorieDisponibili)
                    
                    magazzino = funzioni.rimuoviCategoria(magazzino, categoria)
                    print("\nCategoria rimossa con successo!")
                
                funzioni.salvaMagazzino(magazzino)
                pause()
            case "5":
                cls()

                funzioni.salvaMagazzino(magazzino)
                funzioni.salvaMagazzinoTxt(magazzino)

                print("Magazzino salvato correttamente nel file magazzino.txt!")
                pause()
            case "0":
                cls()

                esci = True
                funzioni.esci()

if __name__ == "__main__":
    main()