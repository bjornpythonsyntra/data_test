#war : write, append, read. 
bestand = open("tekst.txt","w")


# hoe een lijst met items wegschrijven naar txt bestand.
namen = ["An","Bert","Cedric","Dennis","Eric","Frank"]
for naam in namen:
    bestand.write(f"{naam},")
"""
#emum
for e,naam in enumerate(namen):
    bestand.write(f"{e} {naam} ,")"""
