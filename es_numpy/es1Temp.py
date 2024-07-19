"""
Esercizio su Numpy

Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.

Compiti:
Crea una dataset di dati da almeno 24 posizioni
Calcola la temperatura media 
Trova la temperatura massima e minima.
Determina la temperatura più probabile per le prossime 4 posizioni rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana.
"""


import numpy as np

temperature = np.array([
    22.1, 22.3, 22.5, 22.4, 22.6, 22.7, 22.9, 23.0,
    23.2, 23.4, 23.5, 23.6, 23.7, 23.8, 23.9, 24.0,
    24.1, 24.2, 24.3, 24.4, 24.5, 24.6, 24.7, 24.8
])

print(f"Temperature registrate durante la giornata (ogni temperatura fa riferimento ad un'ora della giornata): \n{temperature} \n")

media_temperatura = np.mean(temperature)    #mean per la media
print(f"Temperatura Media: {media_temperatura:.2f} °C")

min_temperatura = np.min(temperature)   #min per la temp minima
print(f"Temperatura Minima: {min_temperatura:.2f} °C")

max_temperatura = np.max(temperature)   #max per la temp massima
print(f"Temperatura Massima: {max_temperatura:.2f} °C")

