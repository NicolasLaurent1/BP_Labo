# Dit is commentaar (coppentarieer je programma)
# Labo_intro Oef1


naam=input("Wat is jouw naam?")
voornaam=input("Wat is uw voornaam?")
leeftijd=int(input("Wat is uw leeftijd"))
print(type(leeftijd))
leeftijd= leeftijd + 10
# voornaam = "Nicolas"
#naam = "Laurent"

#print("Welkom", voornaam, naam)

print( "Welkom {0}. Jouw naam is {1} en je bent {2:.2f} jaar".format(voornaam, naam, leeftijd))

