#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:17:21 2025
Abfluss Modell Übung 6
@author: anabastos
"""
### Packages importieren
import numpy as np
import matplotlib.pyplot as pl

### Funktion Wasser Bilanz ----------------------------------------------------
### Funktionen ermöglichen es uns, die Wiederholung von Schritten zu vermeiden, 
### wenn wir etwas mehrmals berechnen müssen. Wir definieren sie einmal und rufen 
### sie dann einfach im Hauptskript auf. 
### Die Variablen in der Funktion müssen nicht den gleichen Namen wie im 
### Hauptskript haben. Es ist sogar besser, wenn nicht!
def wasser_bilanz(Zufluss,k):
    
    n_schritte  = len(Zufluss) ### Wie viele Zeitschritte gibt es: wird automatisch berechnet
    
    Vol, Abf    = np.zeros(n_schritte), np.zeros(n_schritte) # Wir starten mit Vektoren die "leer" sind (alles mit 00000)
    
    Vol[0]      = Zufluss[0] # Erster Wert vom Volumen == Zufliuss. In python wird die erste Stelle als "0" bezeichnet
    Abf[0]      = Vol[0]*k   # Gleich für Abfluss
    
    for i in np.arange(1,n_schritte):  ### "Für jeder Schritt ab 2., dann Rechnen wir A und V

        Vol[i]  = Vol[i-1] + + Zufluss[i] - Abf[i-1]
        Abf[i]  = Vol[i]*k
    return Vol, Abf ### Die Funktion gibt dann was Raus
### Ende Funktion Wasser Bilanz -----------------------------------------------

    
    
############################### HAUPTSCRIPT ###################################
    
    
### Übung 1 - Linearspeicher mit 1 Reservoir k = 0.2, 30 Zeitschritte (Tage) 

k                   = 0.2 ### Wert wird als eine Variabel definiert
n_tage              = 30  ### Sowie die Zeitlänge
### Wir initialisieren Niederschlag als ein Array (wie eine Spalte in Excel) 
### mit Null Wetern am Anfang und einer Länge von n_tage. 
### Vorteil: wenn wir eine längere Simulation durchführen können, müssen wir nur 
### n_tage Wert oben ändern

Niederschlag        = np.zeros(n_tage) 
Niederschlag[:10]   = 10. # Wir weisen den ersten zehn Zeitschritten einen Wert von 10 mm zu
zeit                = range(n_tage) ### Zeit wird 0, 1, 2, 3, ... bis n_tage

Volume_1, Abfluss_1 = wasser_bilanz(Niederschlag,k)


### Abbildung 
pl.figure() ### Neues Bild starten
pl.plot(zeit,Niederschlag,'cyan',label='P') # Linieen mit Zeit als x und Niederschlag in y plotten. Farbe cyan, label für die legende
pl.plot(zeit,Volume_1,'g',label='V')
pl.plot(zeit,Abfluss_1,'b',label='A')
pl.legend(loc=1,frameon=False) # Legende
pl.ylabel('mm/d') # Text für y-axis
pl.xlabel('Zeit (d)') # Text für x-axis

### Ende Übung 1 --------------------------------------------------------------


    
### Übung 2 - Linearspeicherkaskade: änlich wie Übung 1.
### Niedershlag, k1 und n_tage schon definiert, müssen wir nichts mehr machen
 
Volume_1, Abfluss_1 = wasser_bilanz(Niederschlag,0.4) # Wir können auch k direkt geben (nicht empfohlen für Komplexe Scripts!)
Volume_2, Abfluss_2 = wasser_bilanz(Abfluss_1,0.3)  # Zufluss Vol2 ist Abfluss von V1

### Neue Abbildung 
pl.figure() ### Neues Bild starten
pl.plot(zeit,Niederschlag,'cyan',label='P') # Linieen mit Zeit als x und Niederschlag in y plotten. Farbe cyan, label für die legende
pl.plot(zeit,Volume_1,'g',label='V1')
pl.plot(zeit,Abfluss_1,'b',label='A1')
pl.plot(zeit,Volume_2,'g',ls='--',label='V2')
pl.plot(zeit,Abfluss_2,'b',ls='--',label='A2')
pl.legend(loc=1,frameon=False) # Legende
pl.ylabel('mm/d') # Text für y-axis
pl.xlabel('Zeit (d)') # Text für x-axis

### Ende Übung 2 --------------------------------------------------------------


##### Vorteil?!  --------------------------------------------------------------
##### Sehr einfach eine Komplexere Kaskade zu Rechnen (1min ein bisschen copy/paste)
Volume_1, Abfluss_1 = wasser_bilanz(Niederschlag,0.1) # Wir können auch k direkt geben (nicht empfohlen für Komplexe Scripts!)
Volume_2, Abfluss_2 = wasser_bilanz(Abfluss_1,0.2)  # Zufluss Vol2 ist Abfluss von V1
Volume_3, Abfluss_3 = wasser_bilanz(Abfluss_2,0.4)  # Zufluss Vol2 ist Abfluss von V1
Volume_4, Abfluss_4 = wasser_bilanz(Abfluss_3,0.2)  # Zufluss Vol2 ist Abfluss von V1
Volume_5, Abfluss_5 = wasser_bilanz(Abfluss_4,0.)  # Zufluss Vol2 ist Abfluss von V1

### Neue Abbildung 
pl.figure() ### Neues Bild starten
pl.plot(zeit,Niederschlag,'cyan',label='P') # Linieen mit Zeit als x und Niederschlag in y plotten. Farbe cyan, label für die legende
pl.plot(zeit,Abfluss_1,label='A1')
pl.plot(zeit,Abfluss_2,label='A2')
pl.plot(zeit,Abfluss_3,label='A3')
pl.plot(zeit,Abfluss_4,label='A4')
pl.plot(zeit,Abfluss_5,label='A5')
pl.legend(loc=1,frameon=False) # Legende
pl.ylabel('mm/d') # Text für y-axis
pl.xlabel('Zeit (d)') # Text für x-axis

### Kömmentäre machen es auch einfacher die Aufgaben zu Dokumentieren
### Auch besser zu Reproduzieren
### Felher werden sofort gezeigr (Code läuft nicht). Versuchen sie, die Funktion
### wasser_bilanz ohne k Wert oder Falscher Name zu geben: nächste Zeilen unkommentieren (# Weg)

# wasser_bilanz(Abfluss,k) 
# wasser_bilanz(Niederschlag)