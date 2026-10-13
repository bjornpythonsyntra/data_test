teken = "V"
print(ord(teken))

nummer = 64
print(chr(nummer))

# tekst -> omzetten naar ascii waarde

tekst = "dit is een tekst omgezet naar ascii"
ascii_lijst = []

for teken in tekst:
    ascii_lijst.append(ord(teken))

for nummer in ascii_lijst:
    print(chr(nummer),end=" ")
print("")

# hoe kan dit versleutelen
# hoe kan ik dit ontcijferen. 