"""
Erzeuge Grafiken von LEGO Strassenplatten
"""

from pytamaro.de import (
    Grafik, Farbe,
    weiss, gelb, rgb_farbe, transparent, rgba_farbe,
    kreis_sektor, rechteck, leere_grafik,
    ueberlagere, ueber, neben, fixiere, kombiniere, drehe,
    zeige_grafik, speichere_grafik, speichere_gif,
)

RASEN_FARBE: Farbe = rgb_farbe(0, 203, 109)
STRASSEN_FARBE : Farbe = rgb_farbe(140, 140, 140)
RANDSTREIFEN_FARBE : Farbe= gelb
MITTELSTREIFEN_FARBE : Farbe = weiss


def gruen_grundflaeche(noppengroesse: float,)-> Grafik:
    return rechteck(noppengroesse*32,noppengroesse *32,RASEN_FARBE)

def gerade(noppengroesse: float, ausrichtung : str) -> Grafik:
    if (ausrichtung  == "vertikal" ):
        drehwinkel : int = 90
    else:
        drehwinkel : int = 0
    gruener_streifen : Grafik = gruen_grundflaeche(noppengroesse)
    strassen_streifen : Grafik= rechteck(noppengroesse*32,noppengroesse*20,STRASSEN_FARBE)
    gelber_streifen : Grafik= rechteck(noppengroesse*32, noppengroesse*0.5, RANDSTREIFEN_FARBE)
    mittel_linie : Grafik = rechteck (noppengroesse * 32, noppengroesse *0.5, MITTELSTREIFEN_FARBE)
    gelber_streifen_def : Grafik = ueber(gelber_streifen,ueber(
                            rechteck(noppengroesse*32,noppengroesse*18,transparent),gelber_streifen))
    strassen_elemente : tuple[Grafik]= (mittel_linie,gelber_streifen_def,strassen_streifen, gruener_streifen)
    gerade_strasse: Grafik = leere_grafik()
    for element in strassen_elemente:
        gerade_strasse = ueberlagere(gerade_strasse,element)
    return drehe(drehwinkel,gerade_strasse)
 
def kurve (noppengroesse: float, drehung : int)-> Grafik:
    gruene_flaeche : Grafik = gruen_grundflaeche(noppengroesse)
    gelber_streifen_kurz : Grafik = kreis_sektor(noppengroesse*7,90,gelb)
    gelber_streifen_lang : Grafik = kreis_sektor(noppengroesse*25.5,90, gelb)

    mittel_streifen : Grafik = kreis_sektor(noppengroesse*16.25, 90,MITTELSTREIFEN_FARBE)
    strassen_streifen_komplett: Grafik = kreis_sektor(noppengroesse*26, 90, STRASSEN_FARBE)
    strassen_streifen_rechts : Grafik = kreis_sektor(noppengroesse*25,90,STRASSEN_FARBE)
    strassen_streifen_links :Grafik = kreis_sektor(noppengroesse*15.75,90,STRASSEN_FARBE)
    strassen_streifen_kurz :Grafik = kreis_sektor(noppengroesse*6.5,90,STRASSEN_FARBE)

    gruener_streifen_kurve :Grafik = kreis_sektor(noppengroesse*6,90,RASEN_FARBE)
    alle_elemente : tuple[Grafik] = (gruene_flaeche,strassen_streifen_komplett,gelber_streifen_lang,
                    strassen_streifen_rechts,mittel_streifen,strassen_streifen_links,
                    gelber_streifen_kurz,strassen_streifen_kurz,gruener_streifen_kurve)
    kurve : Grafik = leere_grafik()
    for element in alle_elemente:
        element = fixiere("links", "oben",element)
        kurve = kombiniere(element,kurve)
    return drehe(drehung,kurve)


def fussgaenger_streifen (noppengroesse: float)->Grafik:
    einzel_streife : Grafik = rechteck(noppengroesse,noppengroesse*4,weiss)
    einzel_streife_luecke : Grafik = rechteck(noppengroesse,noppengroesse*4,STRASSEN_FARBE)
    strassen_streife_schmal: Grafik = rechteck(noppengroesse*0.5, noppengroesse*4, STRASSEN_FARBE)
    strassen_streife_oben :Grafik = rechteck(noppengroesse*18,noppengroesse *2,STRASSEN_FARBE)
    strassen_streife_unten : Grafik = rechteck(noppengroesse*18,noppengroesse, STRASSEN_FARBE)
    fussgaenger_streifen : Grafik = strassen_streife_schmal
    for i in range (8):
        fussgaenger_streifen= neben(fussgaenger_streifen,neben(einzel_streife,einzel_streife_luecke))
    fussgaenger_streifen = neben(fussgaenger_streifen,neben(einzel_streife,strassen_streife_schmal))
    fussgaenger_streifen = ueber(strassen_streife_oben,ueber(fussgaenger_streifen,strassen_streife_unten))
    return fussgaenger_streifen

def gruene_ecke(noppengroesse: float)-> Grafik:
    gelbes_rechteck : Grafik = rechteck(noppengroesse*7,noppengroesse*7,gelb)
    graues_rechteck : Grafik = rechteck(noppengroesse*6.5, noppengroesse*6.5,STRASSEN_FARBE)
    gruenes_rechteck : Grafik = rechteck(noppengroesse*6,noppengroesse*6,RASEN_FARBE)
    alle_rechtecke : tuple[Grafik] =(gelbes_rechteck,graues_rechteck,gruenes_rechteck)
    gruene_ecke : Grafik = leere_grafik()
    for element in alle_rechtecke:
        element = fixiere("links", "unten",element)
        gruene_ecke = kombiniere(element,gruene_ecke)
    return gruene_ecke

def abzweigung(noppengroesse : int, ausrichtung: str)-> Grafik:
    fussgaenger_streifen_fixiert: Grafik = fussgaenger_streifen(noppengroesse)
    gruene_ecke_fixiert : Grafik = gruene_ecke(noppengroesse)
    abzweigung : Grafik = neben(gruene_ecke_fixiert,neben(fussgaenger_streifen_fixiert,drehe(90,gruene_ecke_fixiert)))
    abzweigung : Grafik = kombiniere(fixiere("mitte", "unten", abzweigung),
                    fixiere("mitte", "unten",gerade(noppengroesse,"horizontal")))
    if (ausrichtung == "oben"):
        abzweigung = drehe (180,abzweigung)
    elif(ausrichtung =="links"):
        abzweigung= drehe (270,abzweigung)
    elif(ausrichtung =="rechts"):
        abzweigung= drehe(90,abzweigung)
    
    return abzweigung

def kreuzung(noppengroesse: float)-> Grafik:
   
    linker_streifen_gruen_oben : Grafik= drehe(270,gruene_ecke(noppengroesse))
    linker_streifen_fussgaenger : Grafik = drehe(90,fussgaenger_streifen(noppengroesse))
    linker_streifen_gruen_unten : Grafik = gruene_ecke(noppengroesse)
    elemnete_links : Grafik = ueber(linker_streifen_gruen_oben,ueber(
                    linker_streifen_fussgaenger,linker_streifen_gruen_unten))
    mitte_fussgaenger_oben : Grafik = drehe(180,fussgaenger_streifen(noppengroesse))
    kreuzung_mitte : Grafik  = rechteck(noppengroesse*18,noppengroesse*18,STRASSEN_FARBE)
    mitte_fussgaenger_unten : Grafik = fussgaenger_streifen(noppengroesse)
    elemente_mitte : Grafik  = ueber(mitte_fussgaenger_oben, ueber(kreuzung_mitte,mitte_fussgaenger_unten))
    return neben(elemnete_links,neben(elemente_mitte,drehe(180,elemnete_links)))

def alle_strassen_elemente(noppengroesse : float,) -> dict[Grafik]:
    strassen_elemente : dict[Grafik] = {
        "gruenes_feld"      : gruen_grundflaeche(noppengroesse),
        "gerade_horizontal" : gerade(noppengroesse, "horizontal"),
        "gerade_vertikal"   : gerade(noppengroesse, "vertikal"),
        "kurve_li_oben"     : kurve(noppengroesse, 0),
        "kurve_oben_rechts" : kurve(noppengroesse,270),
        "kurve_rechts_unten": kurve(noppengroesse,180),
        "kurve_unten_links" : kurve(noppengroesse,90),
        "abzweigung_links"  : abzweigung(noppengroesse,"links"),
        "abzweigung_oben"   : abzweigung(noppengroesse, "oben"),
        "abzweigung_rechts" : abzweigung(noppengroesse,"rechts"),
        "abzweiung_unten"   : abzweigung(noppengroesse,"unten"),
        "kreuzung"          : kreuzung(noppengroesse),
    }
    return strassen_elemente



def alle_elemente_zeichen(alle : dict)-> Grafik:
    alle_elemente = leere_grafik()
    for value in alle.values():
        alle_elemente = neben(alle_elemente,value)
    return alle_elemente

def zeichne_rundkurs(noppengroesse: float)->Grafik:
    """
    Anmerkung: Eigentlich könnte man dies mit Wave Function Collapse
    herstellen, aber in pytamaro ist es leider etwas umständlich, 
    ... würde ev. schon gehen, hatte leider 
    keine Muse dazu... hier ist nun eine einfache hardcoded 
    Version.
    """
    alle_strassen_teile : dict[Grafik] = alle_strassen_elemente(noppengroesse)

    gesamte_liste : list[Grafik] =[[
        # erste Zeile
         alle_strassen_teile["gruenes_feld"],
         alle_strassen_teile["kurve_rechts_unten"],
         alle_strassen_teile["abzweiung_unten"],
         alle_strassen_teile["abzweiung_unten"],
         alle_strassen_teile["gerade_horizontal"],
         alle_strassen_teile["kurve_unten_links"]
    ],
    [ # zweite Zeile
         alle_strassen_teile["kurve_rechts_unten"],
         alle_strassen_teile["abzweigung_oben"],
         alle_strassen_teile["kreuzung"],
         alle_strassen_teile["abzweigung_links"],
         alle_strassen_teile["gruenes_feld"],
         alle_strassen_teile["gerade_vertikal"] 
    ],
     [ # dritte Zeile
         alle_strassen_teile["gerade_vertikal"],
         alle_strassen_teile["gruenes_feld"],
         alle_strassen_teile["gerade_vertikal"],
         alle_strassen_teile["abzweigung_rechts"],
         alle_strassen_teile["gerade_horizontal"],
         alle_strassen_teile["kurve_li_oben"] 
    ],
    [ # vierte Zeile
         alle_strassen_teile["kurve_oben_rechts"],
         alle_strassen_teile["gerade_horizontal"],
         alle_strassen_teile["abzweigung_oben"],
         alle_strassen_teile["kurve_li_oben"],
         alle_strassen_teile["gruenes_feld"],
         alle_strassen_teile["gruenes_feld"] 
    ]]
    zeile_grafik = leere_grafik()
    gesamte_grafik= leere_grafik()
    for i in range(4):
       for j in range (6):
            zeile_grafik = neben(zeile_grafik,gesamte_liste[i][j])
       gesamte_grafik = ueber(gesamte_grafik,zeile_grafik)
       zeile_grafik = leere_grafik()
        
       
    
        
    
    return gesamte_grafik

speichere_grafik("rundkurs",zeichne_rundkurs(20))
