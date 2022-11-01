from sys import exit
#import inflect extension
import inflect
p = inflect.engine()

# Create a list with names inputted
names = []

# Loop forever until except take place
while True:
    try:
        # Ask for a name
        name = input("Name: ")
        # Append name to names
        names.append(name)
    except:
        # Check, if len of names is less than 1 - pass
        if len(names) < 1:
            pass
        # Make new list with inflect
        mylist = p.join((names))
        # Print new line
        print()
        # Print result
        print("Adieu, adieu, to ", end="")
        print(mylist)
        # Exit 
        exit(0)