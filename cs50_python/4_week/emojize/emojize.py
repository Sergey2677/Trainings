# import emoji extension
import emoji
# Ask for input with emoji
text = input("Input: ")
# Create a variable with new text, part of which is converted into emoji
text_emoji = emoji.emojize(f'Output: {text}')
# Print result
print(text_emoji)