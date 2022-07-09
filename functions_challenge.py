# Define a function called uppercase_and_reverse that takes a little bit of
# text, uppercases it all, and then reverses it (flips all the letters
# around). EG: uppercase_and_reverse("Do not go gentle into that good night.")
# "THGIN DOOG TAHT OTNI ELTNEG OG TON OD"

# adding .lower lowercases words, so maybe .upper uppercases them
# adding .reversed reverses a list.

def uppercase_and_reverse(word):
    word = word.upper()
    word = "".join(reversed(word))
    return word

#string = "banana"

#print(string.upper())

#print("".join(reversed(string)))

print(uppercase_and_reverse("banana"))
print(uppercase_and_reverse("hickory is the neediest baby"))