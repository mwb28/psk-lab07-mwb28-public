"""
Erzeuge eine Grafik von zwei Augen
"""

from pytamaro.de import (
    Grafik, Farbe,
    weiss, schwarz, rgb_farbe, transparent,
    ellipse, rechteck,
    ueberlagere, neben,
    zeige_grafik, speichere_grafik,leere_grafik
)


def auge(durchmesser: float, farbe: Farbe) -> Grafik:
    assert durchmesser > 0
    augen_farben : dict = {2:schwarz,1:farbe, 0:weiss}
    auge : Grafik =leere_grafik()
    for i in range (2,-1,-1):
        auge = ueberlagere(auge,ellipse(durchmesser/(2**i),durchmesser/(2**i),augen_farben[i]))
    return auge

def augen(durchmesser: float, farbe: Farbe) -> Grafik:
    abstand : Grafik = rechteck(durchmesser/3,1,transparent)
    augen_liste : list[Grafik] =[]
    for i in range(2):
        augen_liste.append(auge(durchmesser,farbe))
    return neben(augen_liste[0],neben(abstand,augen_liste[1]))

def augenfarbe(rot: int, gruen: int, blau : int)-> Farbe:
    return rgb_farbe(rot,gruen, blau)

zeige_grafik(augen(200, augenfarbe(100,50,25)))