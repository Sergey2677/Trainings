import random

# Loop forever until inputted a number of level bigger than 0
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass
    
# Create a random number between 1 to level value
random_number = random.randint(1, level)

# Loop forever until level and guess aren't equal
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            elif guess == random_number:
                print("Just right!")
                break
    except:
        pass







