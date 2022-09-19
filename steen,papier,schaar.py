# importeerd de module random
import random

print("Welkom bij steen, papier, schaar.")
#houdt de score bij van winst/verlies of gelijkspel
gebruiker_wins = 0
computer_wins = 0
gelijkgespeeld = 0

#we maken een lijst met alles opties van steen papier schaar voor de gebruiker
opties = ["steen", "papier", "schaar"]

#while loop om een loop te maken van steen papier schaar. stopt niet todat we q drukken, dan breakt hij namelijk.
while True:
    #we maken de input lower zodat de gebruiker geen last heeft als hij perongeluk een letter met hoofdletter heeft gedaan.
    #als de gebruiker bijv. "STEEN" invoert dan verandert de lower() functie hem naar gewoon "steen".
    gerbuiker_input = input("Maak je keuze (steen, papier, schaar) of Q om te stoppen: ").lower()
    #de computer moet ook een keuze maken. We gebruiken random om een getal tussen de 0 en 2 te creëren. dit doe je met random.randint
    #normaal bij een lijst kan je bijv.; lijst[0] gebruiken zodat je alleen de eerste inhoud hebt van de lijst, of lijst[1] om de 2e inhoud etc.
    #In dit voorbeeld hebben we 3 keuzes. 0,1 en 2.  0 = "steen", 1 = "papier" en 2 = "schaar"
    #we zeggen dus de naam van onze lijst in dit geval "opties" en dan de random keuze die door de functie "random.randint" is gemaakt. 
    #we noemen deze variabel computer_keuze
    random_keuze = random.randint(0,2)
    computer_keuze = opties[random_keuze]
    #als de gebruiker op q drukt stopt de while loop,door "break"
    if gerbuiker_input == "q":
        break
    #de gebruiker mag alleen steen,papierof schaar intoetsen. Als dat niet gebeurd dan runt de code opnieuw 
    elif gerbuiker_input not in opties:
        print("Ongeldige Keuze! Kies steen,papier of schaar aub.")
        continue
  
 #winst gebruiker   
    elif gerbuiker_input == "steen" and computer_keuze == "schaar":
        print(f"Je hebt gewonnen de computer had {computer_keuze}.")
        gebruiker_wins = gebruiker_wins + 1

    elif gerbuiker_input == "papier" and computer_keuze == "steen":
        print(f"Je hebt gewonnen de computer had {computer_keuze}.")
        gebruiker_wins = gebruiker_wins + 1

    elif gerbuiker_input == "schaar" and computer_keuze == "papier":
        print(f"Je hebt gewonnen de computer had {computer_keuze}.")
        gebruiker_wins = gebruiker_wins + 1
    
#gelijkspel
    elif gerbuiker_input == "steen" and computer_keuze == "steen":
        print(f"Je hebt gelijkgespeeld de computer had ook {computer_keuze}.")
        gelijkgespeeld = gelijkgespeeld + 1

    elif gerbuiker_input == "papier" and computer_keuze == "papier":
        print(f"Je hebt gelijkgespeeld de computer had ook {computer_keuze}.")
        gelijkgespeeld = gelijkgespeeld + 1

    elif gerbuiker_input == "schaar" and computer_keuze == "schaar":
        print(f"Je hebt gelijkgespeeld de computer had ook {computer_keuze}.")
        gelijkgespeeld = gelijkgespeeld + 1
  
#verlies gebruiker
    else:
        print(f"Je hebt verloren, de computer had {computer_keuze}.")
        computer_wins = computer_wins +1
        
    
print(f"De gebruiker heeft {gebruiker_wins} keer gewonnen.\n"
f"De computer heeft {computer_wins} keer gewonnen.\n"
f"Jullie hebben {gelijkgespeeld} keer gelijkgespeeld.")

    
    
    
