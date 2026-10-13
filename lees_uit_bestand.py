bestand = open("tekst.txt","r")

tekst = bestand.read()
lijnen = tekst.split(",")
print(*lijnen)