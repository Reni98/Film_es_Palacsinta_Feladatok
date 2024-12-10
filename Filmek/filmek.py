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

        filmek.append([cim,rendezo,foszereplo,ev, perc])

legrovidebbfilm = float("inf")
legrovidebbcim = ""
legalabb110perces= 0
filmajanlo = []
szineszek= []
szinesznev= input("Adj meg egy színész nevet: ")
for film in filmek:
    hossz = len(film[0])
    if hossz < legrovidebbfilm:
        legrovidebbfilm = len(film[0])
        legrovidebbcim = film[0]

    if film[4] >= 110:
        legalabb110perces+=1
    
    if film[2] == szinesznev:
        filmajanlo.append(film[0])

with open("filmajanlo.txt", "w", encoding="UTF8") as file:

    if len(filmajanlo) > 0:
        print(";".join(map(str,filmajanlo)))
        file.write(";".join(map(str,filmajanlo)))
    else:
        print(f"Nincs ilyen szinész a listában.")


with open("szineszekesfilmjeik.txt", "w", encoding="UTF8") as f:
    for szin in filmek:
        filmgyülytemeny = []
        szineszek.append(szin[2])
        for sz in szineszek:
            if sz == szin[2] and szin[0] not in filmgyülytemeny:
                filmgyülytemeny.append(szin[0])
                for gy in filmgyülytemeny:
                        f.write(f"\n{sz}: {gy}")
                        
print(f"A legrövidebb cím: {legrovidebbcim}")
print(f"A 110 perces filmek száma: {legalabb110perces}")
