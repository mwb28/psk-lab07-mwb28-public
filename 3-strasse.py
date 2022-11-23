"""
Erzeuge Grafiken von LEGO Strassenplatten
"""

from pytamaro.de import (
    Grafik, Farbe,
    weiss, gelb, rgb_farbe, transparent, rgba_farbe,
    kreis_sektor, rechteck, ellipse, leere_grafik,
    ueberlagere, ueber, neben, fixiere, kombiniere, drehe,
    zeige_grafik, speichere_grafik, speichere_gif,
)

RASEN_FARBE = rgb_farbe(0, 203, 109)
STRASSEN_FARBE = rgb_farbe(140, 140, 140)
RANDSTREIFEN_FARBE = gelb
MITTELSTREIFEN_FARBE = weiss


def gerade(noppengroesse: float) -> Grafik:
    plattengroesse = noppengroesse * 32 # Platte ist 32*32 Noppen gross
    streifenbreite = noppengroesse * 0.5
    # TODO
