# This method breaks up text into words for us
def break_words(text):
    words = text.split()
    return words

# Counts the number of words
def count_words(words):
    return len(words)

# Sorts the words (alphabetically)
def sort_words(words):
    words.sort()
    return words

# Takes in a full sentence and returns the sorted words
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

# Prints the first word after popping it off
def print_first_word(words):
    words = words.pop(0)
    print(words)

# Prints the last word after popping it off
def print_last_word(words):
    word = words.pop()
    print(word)

# Prints the first and last words of the sentence
def print_first_and_last_word(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


demitri_martin_joke = "I used to play sports. \nThen I realized you can buy trophies. Now I am good at everything."

print("----------")
print(demitri_martin_joke)
print("----------")

bottles_of_beer = 99
print("This should be ninety-nine:", bottles_of_beer)

def sing(bottles):
    for number in reversed(range(bottles + 1)):
        if number > 0:
            print_verse(number)
        else:
            print_last_verse()

def print_verse(bottles):
    print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")

def print_last_verse():
    print("No more bottles of beer on the wall, no more bottles of beer. \
    \nGo to the store and buy some more, 99 bottles of beer on the wall.\n")

sing(99)


sentence = "I think it's interesting that 'cologne' rhymes with 'alone'"

words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print('"{0}" has {1} words'.format(sentence, count_words(words)))
print("The words are:", words)
print("The sorted words are:", sorted_words)

print_first_word(words)
print_last_word(words)
print_first_and_last_word(sentence)