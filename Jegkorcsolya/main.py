import csv

filename = "rovidprogram.csv"

with open(filename, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';') 
    header = next(reader)  
    found = False  
    
    for row in reader:
        if "HUN" in row:  # Ellenőrizzük az 'Ország' oszlop tartalmát
            found = True
            print(f"Magyarország szerepel a fájlban: {row}")
            break
    
    if not found:
        print("Magyarország nem található a fájlban.")
