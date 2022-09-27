def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting[:5]:
        return 0
    elif 'h' in greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()