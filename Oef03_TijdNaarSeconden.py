dagen =int(input("Geef het aantal dagen op:")) * 60 * 60 * 24
uren = int(input("Geef het aantal uren op:")) * 3600
minuten = int(input("Geef het aantal minuten op:")) * 60
seconden = int(input("Geef het aantal seconden op:"))

tijd = seconden + minuten + uren + dagen
print("Het totale aantal seconden bedraagt {0}".format(tijd))