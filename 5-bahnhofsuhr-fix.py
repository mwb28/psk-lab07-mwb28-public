"""
Erzeuge eine Animation einer Bahnhofsuhr
"""

from pytamaro.de import (
    Grafik, Farbe,
    weiss, schwarz, rot, rgb_farbe, transparent,
    ellipse, rechteck, leere_grafik,
    ueberlagere, kombiniere, fixiere, drehe,ueber,
    zeige_grafik, speichere_gif
)

NENNDURCHMESSER = 600

RING_AUSSEN_RADIUS :float = NENNDURCHMESSER * 0.51

# Abmessungen gemäss Originalskizzen:
# https://www.eguide.ch/en/objekt/sbb-bahnhofsuhr/

RING_INNEN_RADIUS :float = NENNDURCHMESSER * 0.5
STRICH_AUSSEN_RADIUS :float = NENNDURCHMESSER * 0.485

MINUTEN_STRICH_LAENGE :float = NENNDURCHMESSER * 0.035
MINUTEN_STRICH_BREITE :float = NENNDURCHMESSER * 0.014

STUNDEN_STRICH_LAENGE :float = NENNDURCHMESSER * 0.12
STUNDEN_STRICH_BREITE :float = NENNDURCHMESSER * 0.035

MINUTEN_ZEIGER_KURZE_LAENGE :float = NENNDURCHMESSER * 0.12
MINUTEN_ZEIGER_LANGE_LAENGE :float = NENNDURCHMESSER * 0.46
MINUTEN_ZEIGER_BREITE :float = NENNDURCHMESSER * (0.052 + 0.036) / 2

STUNDEN_ZEIGER_KURZE_LAENGE :float = NENNDURCHMESSER * 0.12
STUNDEN_ZEIGER_LANGE_LAENGE :float = NENNDURCHMESSER * 0.32
STUNDEN_ZEIGER_BREITE :float = NENNDURCHMESSER * (0.064 + 0.052) / 2

SEKUNDEN_ZEIGER_KURZE_LAENGE :float = NENNDURCHMESSER * 0.165
SEKUNDEN_ZEIGER_LANGE_LAENGE :float = NENNDURCHMESSER * 0.312
SEKUNDEN_ZEIGER_SCHEIBE_DURCHMESSER :float = NENNDURCHMESSER * 0.105
SEKUNDEN_ZEIGER_BREITE :float = NENNDURCHMESSER * 0.014

def hintergrund() -> Grafik:
  """Weisser Hintergrund und grauer Rand"""
  hintergrund_weiss : Grafik = fixiere("mitte","mitte",rechteck(NENNDURCHMESSER*1.05,NENNDURCHMESSER*1.05,weiss))
  ring_aussen : Grafik = fixiere("mitte","mitte",ellipse(2*RING_AUSSEN_RADIUS,2*RING_AUSSEN_RADIUS,rgb_farbe(128,128,128)))
  ring_innen : Grafik = fixiere("mitte","mitte",ellipse(2*RING_INNEN_RADIUS,2*RING_INNEN_RADIUS,weiss))
  return kombiniere(ring_innen,kombiniere(ring_aussen,hintergrund_weiss))

def zeichne_zeiger(winkel: float, zeiger : str) -> Grafik:

  """
  Stunden oder Minuten-Zeiger
  Die Angabe, ob Minuten oder Stundenzeiger wird mit "minuten" oder "stunden" uebergeben
  :param winkel: Uhrzeit in Winkel gemessen
  :param zeiger: Stunden oder Minutenzeiger
  :returns: den entsprechenden Zeiger mit Winkel  
  """
  assert zeiger == "stunden" or zeiger == "minuten"
  if zeiger == "stunden":
    breite_zeiger :float = STUNDEN_ZEIGER_BREITE
    hoehe_zeiger_kurz :float = STUNDEN_ZEIGER_KURZE_LAENGE
    hoehe_zeiger_lang :float = STUNDEN_ZEIGER_LANGE_LAENGE
  else:
    breite_zeiger :float = MINUTEN_ZEIGER_BREITE
    hoehe_zeiger_kurz :float = MINUTEN_ZEIGER_KURZE_LAENGE
    hoehe_zeiger_lang :float = MINUTEN_ZEIGER_LANGE_LAENGE

  langer_zeiger : Grafik  = rechteck(breite_zeiger,hoehe_zeiger_lang,schwarz)
  kurzer_zeiger : Grafik  = rechteck(breite_zeiger,hoehe_zeiger_kurz,schwarz)
  return drehe(-winkel,kombiniere(
    fixiere("mitte","unten",langer_zeiger),
    fixiere("mitte","oben", kurzer_zeiger)
  ))

def zeichne_sekunden_zeiger(winkel: float):
  langer_sek_zeiger : Grafik  = rechteck(SEKUNDEN_ZEIGER_BREITE,SEKUNDEN_ZEIGER_LANGE_LAENGE,rot)
  kurzer_sek_zeiger : Grafik  = rechteck(SEKUNDEN_ZEIGER_BREITE,SEKUNDEN_ZEIGER_KURZE_LAENGE,rot)
  kreis_sek_zeiger : Grafik  = ellipse(SEKUNDEN_ZEIGER_SCHEIBE_DURCHMESSER,SEKUNDEN_ZEIGER_SCHEIBE_DURCHMESSER,rot)
  kreis_zeiger_lang : Grafik  = ueber(kreis_sek_zeiger,langer_sek_zeiger)
  return drehe (-winkel,kombiniere(
                fixiere("mitte","unten",kreis_zeiger_lang),
                fixiere("mitte","oben",kurzer_sek_zeiger)
                
  ))


def zeichne_striche(stricheAnzeigen: str) -> Grafik:
  """
  Zeichne alle Minunten- oder Stundenstriche, die Angabe muss in den Parameter uebergeben werden
  (siehe assert)
  """
  assert stricheAnzeigen == "minuten" or stricheAnzeigen =="stunden"
  if (stricheAnzeigen == "minuten"):
    breite :float = MINUTEN_STRICH_BREITE
    laenge :float = MINUTEN_STRICH_LAENGE
    schritt :int = 6
  else:
    breite :float= STUNDEN_STRICH_BREITE
    laenge :float= STUNDEN_STRICH_LAENGE
    schritt :int = 30
  striche : Grafik  = rechteck(breite, laenge,schwarz)
  abstand_striche : Grafik = rechteck(breite,
                2 *STRICH_AUSSEN_RADIUS - 2* laenge,transparent)
  striche_abstand  : Grafik = ueber(striche,ueber(abstand_striche,striche ))
  alle_striche : list[Grafik] = []
  for i in range (0,180,schritt):
    alle_striche.append(drehe(i,striche_abstand))
 
  zeichne_alle_striche : Grafik = leere_grafik()
  for element in alle_striche:
    zeichne_alle_striche = ueberlagere(element,zeichne_alle_striche)
  return fixiere("mitte","mitte",zeichne_alle_striche)


def zeichne_uhr_ohne()-> Grafik:
  return kombiniere(zeichne_striche("stunden"),kombiniere(zeichne_striche("minuten"),hintergrund()))


def zeichne_uhr_mit()-> Grafik:
  minuten_zeiger : Grafik = zeichne_zeiger(20,"minuten")
  stunde_zeiger : Grafik = zeichne_zeiger (275,"stunden")
  sekunden_zeiger : Grafik =  zeichne_sekunden_zeiger(90)
  hintergrund_def : Grafik = zeichne_uhr_ohne()
  return kombiniere(sekunden_zeiger,kombiniere(minuten_zeiger,kombiniere(stunde_zeiger,hintergrund_def)))


def zeichne_uhrzeit(stunden: int, minuten : int, sekunden : int)-> Grafik:
  minuten_zeiger : Grafik = zeichne_zeiger(minuten*6,"minuten")
  sekunden_zeiger : Grafik = zeichne_sekunden_zeiger(sekunden*6)
  stunden_zeiger : Grafik = zeichne_zeiger(stunden*30 +(minuten/2),"stunden")
  hintergrund_def : Grafik = zeichne_uhr_ohne()
  return kombiniere(sekunden_zeiger,kombiniere(minuten_zeiger,kombiniere(stunden_zeiger,hintergrund_def)))


def animierte_uhr ()-> list[Grafik]:
  list_uhr : list[Grafik] = []
  for stunden in range (0,12):
    for min in range (0,60):
        list_uhr.append(zeichne_uhrzeit(stunden,min,0))
  return list_uhr


# speichere_gif("around_the_clock",animierte_uhr(),50)

zeige_grafik(zeichne_uhrzeit(4,30,45))