"""
Erzeuge eine Animation von zwei rollenden Augen
"""

from pytamaro.de import (
    Grafik, Farbe,
    weiss, schwarz, rgb_farbe, transparent,
    ellipse, rechteck,
    ueberlagere, neben, fixiere, kombiniere, drehe,
     speichere_gif
)

def auge(durchmesser: float, augenwinkel: int, farbe: Farbe) -> Grafik:
    assert durchmesser > 0
    pupille : Grafik= ellipse(durchmesser/4,durchmesser/4, schwarz)
    pupille_iris : Grafik = ueberlagere(pupille,ellipse(durchmesser/2,durchmesser/2,farbe))
    sklera : Grafik = ellipse(durchmesser, durchmesser, weiss)

    return drehe(augenwinkel,kombiniere(fixiere("rechts","mitte", pupille_iris),
            fixiere("rechts","mitte",sklera)))


def augen(durchmesser: float, augenwinkel: int, farbe: Farbe) -> Grafik:
    abstand : Grafik = rechteck(durchmesser/3,1,transparent)
    augen_liste : list[Grafik] =[]
    for i in range(2):
        augen_liste.append(auge(durchmesser,augenwinkel,farbe))
    return neben(augen_liste[0],neben(abstand,augen_liste[1]))

def augenfarbe(rot: int, gruen: int, blau : int)-> Farbe:
    return rgb_farbe(rot,gruen, blau)


def rollende_augen_frames(durchmesser : float, farbe: Farbe)-> list[Grafik]:
    list_augen = []
    for winkel in range (0,360,10):
        list_augen.append(augen(durchmesser,winkel,farbe))
    return list_augen

speichere_gif("rollende-augen",rollende_augen_frames(200,augenfarbe(255,255,0)),30)