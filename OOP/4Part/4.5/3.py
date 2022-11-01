balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n: int):
    global balance
    balance += n


def withdraw(n: int):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
