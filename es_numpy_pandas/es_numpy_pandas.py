"""
Esercizio Integrato su Pandas e Numpy

Scenario: Una azienda vuole analizzare la performance giornaliera delle vendite e delle ore lavorative dei suoi dipendenti 
per ottimizzare le operazioni.
Obiettivo: Utilizzare Pandas e Numpy per calcolare le vendite medie per ora lavorativa e identificare giorni di alta e bassa efficienza.

Compiti:
Generazione dei Dati:
Utilizza numpy per generare un array di date per 30 giorni.
Genera dati casuali per "Vendite" e "Ore Lavorative" utilizzando numpy per ciascun giorno.
Crea un DataFrame pandas con colonne "Data", "Vendite", "Ore Lavorative".
Analisi delle Vendite:
Calcola le vendite medie per ora lavorativa per ogni giorno.
Identifica i giorni con la massima e la minima
Salva tutti i valori e i risultati su un nuovo file(ES: csv).
"""
import numpy as np
import pandas as pd

def genera_valori():

    start_date = '2024-06-01'
    date_range = np.arange(np.datetime64(start_date), np.datetime64(start_date) + np.timedelta64(30, 'D'))
    date_giorni = [str(date) for date in date_range]
    
    vendite = np.random.randint(0, 100, 30)
    ore_lavorative = np.random.randint(4, 8, 30)

    return date_giorni, vendite, ore_lavorative

def crea_dataset():

    date_giorni, vendite, ore_lavorative = genera_valori()

    data = {
        "Data":date_giorni,
        "Vendite":vendite,
        "Ore":ore_lavorative
    }

    df = pd.DataFrame(data)
    print("DataFrame Iniziale: \n", df.to_string(index=False), "\n")
    return df

def operazioni_filtraggio(df):

    raggruppamento_data = df.groupby(['Ore']).agg({   
            'Vendite': ['mean'],
    })
    print("\nVendite medie raggruppate per Ore: \n", raggruppamento_data, "\n")

    raggruppamento_data = df.groupby(['Data']).agg({   
            'Vendite': ['mean'],
    })
    print("\nVendite medie raggruppate per Data: \n", raggruppamento_data, "\n")

    df['Vendite_per_Ora'] = df['Vendite'] / df['Ore']
    resoconto = df[['Data','Vendite_per_Ora']]
    print("Resoconto delle vendite per ora: \n", resoconto, "\n")
    return resoconto

def resoconto_max_e_min(df):

    resoconto = operazioni_filtraggio(df)

    idmax = resoconto.loc[resoconto['Vendite_per_Ora'].idxmax()]
    idmin = resoconto.loc[resoconto['Vendite_per_Ora'].idxmin()]

    print("Vendite per ora Max: \n", idmax, "\n")
    print("Vendite per ora Min: \n", idmin, "\n")

def salva_nuovo_csv(df):

    df.to_csv('C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\19.07\\es_numpy_pandas\\file_salva.csv', index=False)
    print("DataFrame salvato")  #salvataggio su un nuovo csv
    return df

def menu_pandas():  #menu

    print("\nMenu:")
    print("1. Operazioni di raggruppamento")
    print("2. Filiale con numero maggiore di vendite")


df = crea_dataset()

while True:

    menu = menu_pandas()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: "))
    if opzione == 1:
        operazioni_filtraggio(df)
        salva_nuovo_csv(df)
    elif opzione == 2:
        resoconto_max_e_min(df)
        salva_nuovo_csv(df)
    else:
        print("Scelta non disponibile")

    continua = input("Vuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break