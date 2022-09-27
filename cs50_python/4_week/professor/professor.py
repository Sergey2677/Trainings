import random

def main():
    # Ask for level
    level = get_level()
    # Counter for rounds
    count_round = 0
    # Counter for score
    score = 0
    # Loop until count round is bigger or equal than 10
    while count_round < 10:
        # Get random ints
        x, y = generate_integer(level)
        # Bool response
        response = generate_round(x, y)
        # If True + 1 to score value
        if response == True:
            score += 1
        count_round += 1
        # Print result
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def generate_round(x, y):
    incorrect_tries = 1
    while incorrect_tries <= 3:
        try:
            ask_result = int(input(f"{x} + {y} = "))
            if ask_result == (x + y):
                return True
            else:
                print("EEE")
                incorrect_tries += 1
        except:
            print("EEE")
            incorrect_tries += 1
            pass
    print(f"{x} + {y} = {x + y}")
    return False


if __name__ == "__main__":
    main()