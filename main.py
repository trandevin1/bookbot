import sys

def countWords(file):
    return len(file.split())

def countLetters(strings):
    letterCount = {}

    for string in strings:
        for char in string.lower():
            if char in letterCount:
               letterCount[char] += 1
            elif char.isalpha():
               letterCount[char] = 1
    
    return letterCount

def sort_on(tup):
    return tup[1]

def report(letters):
    listOfLetters = [letter for letter in letters.items()]
    print(listOfLetters.sort(reverse=True, key=sort_on))
    print(listOfLetters)


def main():

    print(sys.argv)

    path = sys.argv[1]

    with open(path, 'r') as file:
        file_contents = file.read()

    print(countWords(file_contents))
    letterDict = countLetters(file_contents.split())
    #print(letterDict)
    report(letterDict)



main()
