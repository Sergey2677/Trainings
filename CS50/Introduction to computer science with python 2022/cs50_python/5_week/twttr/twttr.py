def main():
    word = input("Input: ")
    word_new = shorten(word)
    print("Output:", word_new)


def shorten(word):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    for vowel in vowels:
       word = word.replace(vowel,"")
    return word

if __name__ == "__main__":
    main()
