

"""RANDOM GAME GUESSING"""



import random
nums=random.randint(1,10)
print(nums)
tries=0

while True:
    guess=int(input("Please guess your number:"))
    if nums==guess:
        tries+=1
        print(f"YOUR CORRECT\nYOUR TRIES ARE{tries}")
        break

    elif nums>guess:
        tries+=1
        print("go little higher")

    elif nums<guess:
        tries+=1
        print("go little lower")

    else:
        tries+=1
        print("YOUR WRONG")





