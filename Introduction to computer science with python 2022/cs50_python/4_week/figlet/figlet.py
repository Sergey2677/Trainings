import sys
import random
# The documentation for pyfiglet isn’t very clear, but you can use the module as follows
from pyfiglet import Figlet
figlet = Figlet()

# Checks of argv value
if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    random_station = True
elif len(sys.argv) == 1:
    random_station = False
else:
    # Exit if argv value is not correct
    print("Ivalid usage")
    sys.exit(1)

# To set figlet font
if random_station == True:
    figlet.setFont(font=sys.argv[2])
elif random_station == False:
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)

# Input from user
text = input("Input: ")

# Print result
print("Output: ")
print(figlet.renderText(text))

