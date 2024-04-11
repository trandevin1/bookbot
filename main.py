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


def sort_on(dict):
    return list(dict.values())[0]


def report(letters):

    listOfLetters = [{key: value} for key, value in letters.items() if key.isalpha()]
    listOfLetters.sort(reverse=True, key=sort_on)

    print(f"--- Begin Report of {sys.argv[1]} ---")

    for char in listOfLetters:
        key, value = list(char.items())[0]
        print(f"The '{key}' character was found {value} times")

    print("--- END REPORT ---")


def main():

    if len(sys.argv) < 2:
        print("Missing argument please try again!")
        print("Example command: 'python3 main.py <path to book file here>'")
        exit(-1)

    path = sys.argv[1]

    with open(path, "r") as file:
        file_contents = file.read()

    letterDict = countLetters(file_contents.split())
    report(letterDict)


main()
