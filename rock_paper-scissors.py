import random
choices=["rock", "paper", "scissors"]
playerInput= input("Choose rock, paper or scissors: ").lower()
computer= random.choice(choices)

if playerInput== computer:
    print(f"It's a tie, both chose{playerInput}")
elif(playerInput=="" and computer == " ") or (playerInput=="" and computer == " ") or  (playerInput=="" and computer == " "):
   print(f"Congrats, you win! {playerInput} beats {computer}")
else:
    print(f"Wasted.{computer} beats {playerInput}. Try again?")   