"""
Erzeuge eine Animation einer Siebensegmentanzeige
"""

from pytamaro.de import (
    Grafik, zeige_grafik,
    rgb_farbe, transparent,
    rechteck, dreieck, leere_grafik,
    drehe, ueber, neben,
    speichere_gif
)


def segment(breite: float, ein: bool) -> Grafik:
    if (ein):
        segment_dreieck : Grafik = dreieck(breite,rgb_farbe(255,0,0))
        segment_rechteck : Grafik = rechteck(breite,breite*3,rgb_farbe(255,0,0))
    else:
        segment_dreieck : Grafik = dreieck(breite,rgb_farbe(0,0,0))
        segment_rechteck : Grafik = rechteck(breite,breite*3,rgb_farbe(0,0,0))
    return ueber(segment_dreieck,ueber
                (segment_rechteck,drehe(180,segment_dreieck)))


def zeichne_ziffer(breite: float, ziffer : str)->Grafik:
    ziffer : int = int(ziffer)
    ziffern_dekorieren : tuple[bool]= dekoriere(ziffer)

    links_oben  : Grafik= segment(breite,ziffern_dekorieren[0])
    mitte_oben  : Grafik= drehe(90,segment(breite,ziffern_dekorieren[1]))
    rechts_oben : Grafik = segment(breite, ziffern_dekorieren[2])
    mitte : Grafik = drehe(90,segment(breite, ziffern_dekorieren[3]))
    links_unten : Grafik = segment(breite, ziffern_dekorieren[4])
    unten : Grafik = drehe(90,segment(breite, ziffern_dekorieren[5]))
    rechts_unten : Grafik = segment(breite,ziffern_dekorieren[6])
    
    abstands_segment : Grafik = rechteck(breite*5, breite*5,transparent)
    oberes_segment : Grafik= neben(links_oben,neben(abstands_segment,rechts_oben))
    oberes_segment : Grafik = ueber(mitte_oben,oberes_segment)
    unteres_segment  : Grafik= neben(links_unten,neben(abstands_segment,rechts_unten))
    unteres_segment : Grafik = ueber(mitte,ueber(unteres_segment,unten))
   
    return ueber(oberes_segment,unteres_segment)
    

def dekoriere(ziffer: str)-> tuple[bool]:
    """
    Die Eingabe entspricht der Reihenfolge der Funktion zeichne_ziffer
    :param: die Ziffer die dekoriert werden soll. Falls eine Zahl > 9 eingegeben wird,
            wird die Null ausgegeben
    :returns : Tupel mit den Wahrheitswerten, welche Segemente angeschaltet werden.
    """
    ziffer_abs = abs(int(ziffer))

    ziffern_dekorator = (True,True,True,False,True,True,True)
    if (ziffer_abs == 1):
        ziffern_dekorator = (False,False,True,False,False,False,True)
    elif (ziffer_abs == 2):
        ziffern_dekorator = (False,True,True,True,True,True,False)
    elif (ziffer_abs == 3):
        ziffern_dekorator = (False,True,True,True,False,True,True)
    elif (ziffer_abs == 4):
        ziffern_dekorator = (True,False,True,True,False,False,True)
    elif (ziffer_abs == 5):
        ziffern_dekorator = (True,True,False,True,False,True,True)
    elif (ziffer_abs == 6):
        ziffern_dekorator = (True,True,False,True,True,True,True)
    elif (ziffer_abs == 7):
        ziffern_dekorator = (False,True,True,False,False,False,True)
    elif (ziffer_abs == 8):
        ziffern_dekorator = (True,True,True,True,True,True,True)
    elif (ziffer_abs == 9):
        ziffern_dekorator = (True,True,True,True,False,True,True)
    return ziffern_dekorator


def mehrstellige_ziffer(breite : float, zahl: str)-> Grafik:
    """
    Zeigt alle Ziffern hintereinander an, die Ziffern müssen im str Format
    eingegeben werden, da die Null sonst nicht dargestellt werden kann.
    :param breite: die Breite der einzelnen Segmente 
    :param zahl: die Zahl die angezeigt werden soll.
    : returns: die Zahlen in einer Grafik
    """
    full_int : list[str] = []
    
    abstand : Grafik= rechteck(breite*3,breite*13, transparent)
    zeichne_alle_ziffern : Grafik= neben(abstand,leere_grafik())
    zahl= abs(int(zahl))
    for digit in str(zahl):
        full_int.append(int(digit))
    
    for zahl in full_int:
        zeichne_alle_ziffern = neben(zeichne_alle_ziffern,
                                neben(abstand,zeichne_ziffer(breite,zahl)))
    
    return neben(zeichne_alle_ziffern, abstand)

def counter(breite : float, reverse : bool)-> Grafik:
    alle_zahlen = []
    if reverse:
        for i in range(9,-1,-1):
            alle_zahlen.append(zeichne_ziffer(breite,i))
    else:
        for i in range (10):
             alle_zahlen.append(zeichne_ziffer(breite,i))
    
    return alle_zahlen



speichere_gif("counterdown",counter(30,True),500)

zeige_grafik(zeichne_ziffer(30,"-8"))


    
zeige_grafik(mehrstellige_ziffer(30,"4"))
