import sys
import time

def stampaMenu():
    print("--------------------------------------------------------------------")
    print("|                        MENU DELLE OPZIONI                        |")
    print("|                                                                  |")
    print("|  [1] Per modificare una quantità di un articolo                  |")
    print("|  [2] Per aggiungere o rimuovere un articolo                      |")
    print("|  [3] Per stampare l'elenco di articoli di una categoria          |")
    print("|  [4] Per aggiungere o rimuovere una categoria di articoli        |")
    print("|  [5] Per salvare le informazioni di un magazzino in un file .txt |")
    print("|  [0] Per uscire                                                  |")
    print("--------------------------------------------------------------------")
    
def esci():
    print("Grazie per avermi utilizzato! Esco tra 3 secondi...")
    time.sleep(3)
    sys.exit()