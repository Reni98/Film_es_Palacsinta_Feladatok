
"""1.) Olvasd be a mellékelt file (film.txt) tartalmát, majd add meg az adatok sorainak a számát (az első sor nélkül)!
2.) Melyik a legrövidebb film címe?
3.) Hány darab legalább 110 perces film van?
4.) Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből, ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű színész, akkor azt is tudasd!
5.) A 4-es feladat eredményét írasd ki fájlba is! (szorgalmi)
6.) Készíts statisztikát a rendezők alapján! (Hány filmjük szerepel a listában?)
(A feladat nehézségét az adja, hogy előfordul, hogy néhol 2 rendező is fel van tüntetve “, “-vel elválasztva egymástól)"""

filmek = []

with open("film.txt", "r", encoding="UTF8") as fajl:
    sorok = fajl.readlines()

    for sor in sorok[1:]:

        sor = sor.strip()
        sor = sor.split(";")

        cim = sor[0]
        rendezo = sor[1]
        foszereplo = sor[2]
        ev = int(sor[3])
        perc = int(sor[4])

        filmek.append([cim, rendezo, foszereplo,ev,perc])
legrovidebb= float('inf')
legrovidebb_Cim = ""
db= 0
szinesz = input("Adj meg egy színész nevet:")
filszineszek = []
for film in filmek:
    #print(f"{film[0]}, {film[1]}, {film[2]}, {film[3]}, {film[4]}")
    hossz = len(film[0])
    if hossz < legrovidebb:
        legrovidebb = len(film[0])
        legrovidebb_Cim = film[0]
    if film[4] >= 110:
        db+=1
    if film[2] == szinesz:
        filszineszek.append(film[0])

with open("kiirtfilmek.txt", "w", encoding="UTF8") as file:

    if len(filszineszek) > 0:
        print(";".join(map(str,filszineszek[:1])))
        file.write(";".join(map(str,filszineszek[:1])))
    else:
        print("Nincs ilyen személy a listában.")
        file.write("Nincs ilyen személy a listában.")
    
print(f"A legrövidebb film címe: {legrovidebb_Cim}")
print(f"Legalább {db} db 110 perces film van.")
print(f"{len(filmek)}")
