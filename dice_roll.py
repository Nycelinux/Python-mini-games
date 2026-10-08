import random
def roll_dice():
    return random.randint(1,6)
rounds=int(input("How many rounds?"))
target= int(input("Target score to reach: "))

total=0
history=[]
round_num= 0
while total < target and round_num <rounds:
    roll= roll_dice()
    total += roll
    round_num += 1 
    history.append(roll)
    print(f"Round{round_num} rolled {roll}, total = {total}")
if total >= target: 
    print(f"Jackpot! Those dice are smoking hot! You reached {total} in {round_num} rounds.")
else: 
    print(f" Bad luck? Or just a warm up? Roll again! You reached {total} in {round_num} rounds.")
