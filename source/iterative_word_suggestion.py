import time

words = []

with open('EnglishDictionary.csv', mode='r') as csv_file:
    for line in csv_file:
        word, frequency = line.rstrip().split(',')
        words.append([word, frequency])


def suggestions(word):
    word_suggestions = []
    for element, freq in words:
        if(element.startswith(word)):
            word_suggestions.append([element, freq])
    word_suggestions.sort(key=lambda x:x[1], reverse=True)
    return word_suggestions[0:5]

def exiting():
    print("Exiting")
    time.sleep(2)


top_suggestions = []
word = ""
while(1):
    character = input('Enter character and press Enter: ')
    start_time = time.time()
    if(character == '#'):
        exiting()
        break
    if(len(character) is not 1):
        print("Invalid input")
        exiting()
        break

    word = word + character
    print(word)
    top_suggestions = [element[0] for element in suggestions(word)]
    if not top_suggestions:
        print("No match Found !!")
        exiting()
        break
    else:
        print(*top_suggestions, sep=", ", end="")
    print("\t{:.5f}s".format(time.time() - start_time))

