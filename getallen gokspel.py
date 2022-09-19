import random
print("Welkom bij het raadspel")
top_of_range = input("Type een getal: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
        
    if top_of_range <= 0:
        print("Geef een getal groter dan 0 aub")
        quit()
        
else:
    print("Type alleen een getal in aub") 
    quit()
        
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guess = input("Noem een getal: ") 
    if guess.isdigit():
        guess = int(guess)
       
        if guess == random_number:
            guesses = guesses + 1
            print(f"Goed gegokt het was numero {random_number}")
            print(f"Goed je hebt het in {guesses}x geraden")
            break
        elif guess < random_number:
            print('Fout, Hoger')
            guesses = guesses + 1
        elif guess > random_number:
            print('Fout,Lager')
            guesses = guesses + 1
            
    else:
        print("Voer een getal")
   
    
    
    
