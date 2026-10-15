from tabulate import tabulate

headers = ["naam","klas","woonplaats"]
studenten = [

    ["Anke","1a","As"], #0
    ["Ben","1a","Genk"], #1
    ["Cindy","2a","Genk"], # 2
    ["Dirk","2a","Hasselt"], #3
    ["Ebert","2b","Hasselt"],
    ["Fien","2b","Zutendaal"]
]

def toon_alle_leerlingen():
    data = tabulate(studenten,headers=headers)
    print(data)

def toon_alle_namen():
    for e,naam in enumerate(studenten):
        print(e,naam[0])

def return_namen():
    res = []
    for naam in studenten:
        res.append(naam[0])
    return res

def voeg_leerling_toe():
    naam = input("geef de naam")
    klas = input("geef de klas")
    woonplaats = input("geef de woonplaats")
    student = [naam,klas,woonplaats]
    studenten.append(student)

def verwijder_leerling():
    #welke leerling
    toon_alle_namen()
    student_nummer = int(input("geef het nummer van de student"))
    #is het ingegeven nummer kleiner dan het aantal studenten in de lijst
    if student_nummer < len(studenten):
        # verwijder de leerling op basis van de index
        studenten.pop(student_nummer)
    else:
        print("student niet gevonden")

def bestaat_de_leerling():
    #wie
    naam = input("welke naam wie je opzoeken")
    #naam controleren
    if naam in return_namen():
        #op welke plaats/index bevind zich naam x
        plaatsnummer = return_namen().index(naam)#zoek de index van naam in de return lijst van namen
        #feedback bestaat en plaatsnummer
        print(f"{naam} komt voor in de lijst op plaats {plaatsnummer}")
    else:
        print("naam niet gevonden")

def toon_iedereen_van_woonplaats():
    #result voorzien
    res = []
    woonplaats = input("geef de woonplaats")
    #indien de student woont in de gezochte gemeente. dan toegevoegd aan de lijst
    for student in studenten:
        if woonplaats == student[2]:
            res.append(student)
    print(tabulate(res,headers=headers))

def verander_klas_van_leerling():
    #welke leerling
    toon_alle_namen()
    student_nummer = int(input("geef het nummer van de student"))
    if student_nummer < len(studenten):
        # nieuwe klas klas toevoegen vragen welke nieuwe en koppelen aan studen
        nieuwe_klas = input("geef de nieuwe klas")
        studenten[student_nummer][1] = nieuwe_klas
    else:
        print("ongeldig student nummer")



verander_klas_van_leerling()
toon_alle_leerlingen()