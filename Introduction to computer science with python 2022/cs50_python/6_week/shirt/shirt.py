from sys import argv, exit
from PIL import Image, ImageOps
from os.path import splitext

def main():
    # Check comand-line args
    check_comand_line_arguments()
    try:
        # Try open file with name of argv[1]
        before = Image.open(f"{argv[1]}")
    except FileNotFoundError:
        # If an error has occurred
        print("File not found")
        exit(1)
    # Open image with shirt
    shirt = Image.open("shirt.png")
    # Resize and crop before image to shirt's size
    before = ImageOps.fit(before, shirt.size)
    # Paste shirt to before image
    before.paste(shirt, shirt)
    # Save result
    before.save(f"{argv[2]}")





# Fucnt to check comand-line args
def check_comand_line_arguments():
    if len(argv) > 4:
        print("Too many command-line arguments")
        exit(1)
    elif len(argv) < 3:
        print("Too few command-line arguments")
        exit(1)
    # Split arg between dot
    arg1 = splitext(argv[1])
    # Split arg between dot
    arg2 = splitext(argv[2])
    # Check are args right extension
    if check_extension(arg1[1].lower()) == False or check_extension(arg2[1].lower()) == False:
        print("Not a Image file")
        exit(1)
    # Check are argv[1] and argv[2] the same
    if arg1[1].lower() != arg2[1].lower():
        print("Input and output have different extensions")
        exit(1)


# Bool Check extension
def check_extension(arg):
    if arg in [".jpg", ".jpeg",".png"]:
        return True
    return False

main()