import validators

email = input("What's your email address? ")


try:
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")
except:
    print("Invalid")




