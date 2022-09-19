
wil_de_gebruiker_spelen = input("Wil je de quiz spelen (ja/nee): ")

#!= als de gebruiker neit wil spelen, stopt de code., als hij wel wilt spelen runt de code door en begint het spel.
#.lower() zorgt ervoor dat het antwoord van de gebruiker gelowered word. 
#dus Als hij JA of Ja typt word het veranderd naar ja.
#zonder deze .lower() zou hij Ja of JA meerekenen als nee en dus de code quitten
if wil_de_gebruiker_spelen.lower() != "ja":
    print("Jammer dat je niet wil spelen")
    quit()

print("Welkom bij de quiz")
#hier zie je de lower() weer.

#we gaan een score bijhouden
score = 0

vraag_1 = input("Wat is de hoofdstad van Nederland: ")
if vraag_1.lower() == "amsterdam":
    print("Juist")
#als de gebruiker het goede antwoord geeft, komt er bij de score 1 bij.    
    score = score + 1
else:
    print("Onjuist")

vraag_2 = input("Welke kleur hebben de ruiten in een kaartspel: ")
if vraag_2.lower() == "rood":
    print("Juist")
#als de gebruiker het goede antwoord geeft, komt er bij de score 1 bij.    
    score = score + 1    
else:
    print("Onjuist")
    
vraag_3 = input("In welk tv-programma kom je Tommy, Ienie Minie en Pino tegen: ")
if vraag_3.lower() == "sesamstraat":
    print("Juist")
#als de gebruiker het goede antwoord geeft, komt er bij de score 1 bij.    
    score = score + 1    
else:
    print("Onjuist")
    
vraag_4 = input("Welke toets vind je op een toetsenbord tussen de “E” en de “T”: ")
if vraag_4.lower() == "r":
    print("Juist")
#als de gebruiker het goede antwoord geeft, komt er bij de score 1 bij.    
    score = score + 1    
else:
    print("Onjuist")
    
vraag_5 = input("Naar welke Romeinse god is de maand maart vernoemd: ")
if vraag_5.lower() == "mars":
    print("Juist")
#als de gebruiker het goede antwoord geeft, komt er bij de score 1 bij.    
    score = score + 1    
else:
    print("Onjuist")    
    
#met een f string zorg je ervoor dat je bijv. een string kan gebruken met ints of andere parameters.
#percentage word berekend door de score te delen met het aantal bestaande vragen keer 100
# we voegen int toe om het minimalistischer te maken want dat zorgt ervoor dat je er een heel getal uitkomt.
# als je de int niet zou gebruiken zou er een float als getal komen dus bijv: 40.0 %.
print(f"Je hebt {score} vragen goed. Dit is een percentage van {int(score/5 * 100)}%")    
    
    
    
    
    
