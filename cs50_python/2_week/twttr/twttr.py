# Letters to filter out
vowels = ['a','A','e','E','i','I','o','O','u','U']

# Ask for text
text = input("Input: ")

# Replace all vovels
for vowel in vowels:
       text = text.replace(vowel,"")
# Print result
print("Output:", text)