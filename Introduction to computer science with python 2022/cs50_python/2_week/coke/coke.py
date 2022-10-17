
# Cost of coke
amount_due = 50

# Loop forever until we break at some point
while True:
    print("Amount Due:", amount_due)
# Ask user to insert coin
    inserted_coin = int(input("Insert coin: "))
# Check is there correct value of input coins
    if inserted_coin in [5, 10, 25]:
        amount_due -= inserted_coin
# Print if there is no change owed
    if amount_due == 0:
        print("Change owed: 0")
        break
# Print amount of change owed
    elif amount_due < 0:
        print("Change owed:", abs(amount_due))
        break