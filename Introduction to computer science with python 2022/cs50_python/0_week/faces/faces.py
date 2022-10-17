
# main function
def main():
    # input any text
    text = str(input())
    convert(text)

# replace symbols
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

# call main function
main()