input = input("Greeting: ").lower().strip()
if 'hello' in input[:5]:
    print("$0")
elif 'h' in input[0]:
    print("$20")
else:
    print("$100")