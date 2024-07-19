"""
Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

Compiti:
Genera i dati da un file CSV.
Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
Calcola la media delle vendite giornaliere per filiale
Calcola quale filiale ha venduto di più
Salva tutti i valori e i risultati su un nuovo file(ES: csv).
"""

import pandas as pd

def carica_da_csv():    #funzione per caricare il csv
    file_path = 'C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\es_pandas\\vendite_filiali.csv'
    df = pd.read_csv(file_path)
    return df

def raggruppamento(df):   #raggruppamento per churn ritornando media, mediana e std delle colonne selezionate

    grouped_df = df.groupby('Data').sum()   #raggruppamento per data
    grouped_df2 = df.groupby('Filiale').sum()   #raggruppamento per filiale
    print(grouped_df, "\n")
    print(grouped_df2, "\n")


    raggruppamento_data = df.groupby('Data').agg({   #vendite medie per data
            'Vendite': ['mean'],
    })
    print("\nVendite medie raggruppate per Data: \n", raggruppamento_data, "\n")

    raggruppamento_filiale = df.groupby('Filiale').agg({    #vendite medie per filiale
            'Vendite': ['mean'],
    })
    print("\nVendite medie raggruppate per Filiale: \n", raggruppamento_filiale, "\n")

    risultati_raggruppamento = pd.concat([
        raggruppamento_data.rename(columns={'Vendite': 'Vendite_Media_Data'}),  #concatenazione dei risultati
        raggruppamento_filiale.rename(columns={'Vendite': 'Vendite_Media_Filiale'})
    ], axis=1).reset_index()

    return risultati_raggruppamento


def filiale_maggiore_vendite(df):

    totali_filiale = df.groupby('Filiale').agg({'Vendite': 'sum'}).reset_index()    #raggruppa per filiale e fa la somma delle vendite
    filiale_max_vendite = totali_filiale.loc[totali_filiale['Vendite'].idxmax()]    #tramite loc accede alla riga in totali filiale e ritorna il massimo id
    print("\nFiliale con le vendite più alte:\n", filiale_max_vendite, "\n")    #stampa il maggiore
    return filiale_max_vendite

def salva_nuovo_csv(df):

    df.to_csv('C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\18.07\\es_pandas\\vendite_filiali_aggiornato.csv', index=False)
    print("DataFrame salvato")  #salvataggio su un nuovo csv
    return df

def menu_pandas():  #menu

    print("\nMenu:")
    print("1. Operazioni di raggruppamento")
    print("2. Filiale con numero maggiore di vendite")

df = carica_da_csv()

while True:

    menu = menu_pandas()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: ")) #scelta opzione
    if opzione == 1:
        raggruppamento(df)  #raggruppa
        df = raggruppamento(df) #mette il valore ritornato in df
        salva_nuovo_csv(df) #salva df
    elif opzione == 2:
        df = carica_da_csv()    #riprende il df iniziale (perchè se faccio prima l'operazione 1 e poi la 2 non riconosce il csv)
        filiale_maggiore_vendite(df)    #filtra
        df = filiale_maggiore_vendite(df)   #riassegna il df con il valore filtrato 
        salva_nuovo_csv(df) #stampa
    else:
        print("Scelta non disponibile")

    continua = input("Vuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break