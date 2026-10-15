teken = "V"
print(ord(teken)) # teken naar ascii waarde te gaan

nummer = 64
print(chr(nummer)) # ascii naar teken te gaan

# tekst -> omzetten naar ascii waarde

tekst = "dit is een tekst omgezet naar ascii"
ascii_lijst = []

for teken in tekst:
    waarde = bin(ord(teken))
    ascii_lijst.append(waarde[2:])

print(ascii_lijst)


for nummer in ascii_lijst:
    print(chr(nummer),end=" ")
print("")

# hoe kan dit versleutelen
# hoe kan ik dit ontcijferen.
# let error is er omdat binair een string is en string kan niet omgezet woorden naar getal