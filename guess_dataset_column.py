import random
columns=["customer_id","name","first_name","birth_date","order_id","order_date","product_name","product_id","price","status","quantity", "total", "category", "email"]
word= random.choice(columns)
guessed= set()
attempts=8

while attempts > 0:
    display= " ".join(c if c in guessed else "_" for c in word)
    print(f"word: {display} Attempts left: {attempts}")
    guess= input("Guess a letter : ").lower()
    if guess in guessed:
        print("You already guessed the letter. Try again")
        continue
    guessed.add(guess)
    if guess not in word:
        attempts -=1
        print("not in the word")

    if all(c in guessed for c in word ): 
        print(f"\n You win! The word was  '{word}'.")
        break

else: 
    print(f"\n Out of attempts, the word was '{word}'.")