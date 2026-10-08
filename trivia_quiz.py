import random
quizQuestions = {
    "What is the name of Mario's dinosaur friend?": "Yoshi",
    "Which blocky game is the best-selling video game of all time?": "Minecraft",
    "In 'Rock Paper Scissors', what does Paper always defeat?": "Rock",
    "How many dots are on a standard six-sided die?": "21",
    "What is the name of the green hero in 'The Legend of Zelda'?": "Link",
    "What does RNG stand for in gaming?": "Random Number Generator",
    "Which Pokémon is known as number 025 in the Pokédex?": "Pikachu",
    "In Dungeons & Dragons, what is a perfect roll on a d20 called?": "Critical Hit",
    "What is the ultimate answer to life, the universe, and everything?": "42",
    "Which company created the PlayStation?": "Sony",
    "What is the name of Sonic the Hedgehog's yellow sidekick?": "Tails",
    "In Pac-Man, what is the name of the red ghost?": "Blinky",
    "How many players are on the field for one team in a soccer match?": "11",
    "What device do you roll in Yahtzee or Kniffel?": "Dice",
    "What is the main currency used in the game Roblox?": "Robux"
}

correctMessages = [
    "Boom! Mind reading status: Unlocked.",
    "Calculated. Precise. Lethal. Correct!",
    "RNGesus has blessed your brain cells!",
    "Flawless victory! You read that question like an open book.",
    "Pure skill. (Okay, maybe a little luck too).",
    "Critical Hit! You answered like a god.",
    "Winner winner, chicken dinner!",
    "Boom Shakalaka! That's correct!"
]

wrongMessages = [
    "The AI read you like an open book. Try again!",
    "Wasted. That was not the right answer.",
    "Computer: 1, Human: 0. The robot uprising continues.",
    "Oops! Your brain cells weren't dynamic enough.",
    "Calculated, predicted, defeated. Wrong answer!",
    "Is that your best move? Try harder next time!",
    "Not your best round. Ready to redeem yourself?",
    "Mission Failed. We’ll get ’em next time!"
]

def play_quiz(): 
    max_questions=len(quizQuestions)
    rounds=int(input("How many questions do you want? Max{max_questions}): ")) 
    if rounds > max_questions: 
        rounds= max_questions
    score=0
    
    selected_questions= random.sample(list(quizQuestions.items()), rounds)
    for round_num, (question, answer) in enumerate(selected_questions, start=1):
     
        user_input= input(f"Question {round_num}: {question} \n Your answer: ").strip()
        if user_input.lower() == answer.lower():
            randomLob = random.choice(correctMessages)
            print(f"\n {randomLob}")
            score +=1 
        else:
            randomFrust = random.choice(wrongMessages)  
            print(f"\n{randomFrust}, the correct answer was: {answer}")


    print(f"Your final score is score:{score}/{rounds}") 

play_quiz()