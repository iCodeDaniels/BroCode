# EMOJI FACE CONVERTER
message = input("> ")
words = message.split(' ')
emojis = {
     ":)": "LOL",
     ":(": "SMH"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

