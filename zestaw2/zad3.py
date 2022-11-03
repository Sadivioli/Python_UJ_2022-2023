

def main():
    userInput = input("Wpisz ciąg znaków (składnia: A-Z, a-z, 0-9): ")

    words = 0
    letters = 0
    numbers = 0
    usedCharacters = {}
    
    for i in userInput:
        if i.isalpha():
            letters += 1
            if i in usedCharacters:
                usedCharacters[i] += 1
            else:
                usedCharacters[i] = 1
        elif i.isdigit():
            numbers += 1
        elif i.isspace():
            words += 1
    
    
    print("Liczba słów: ", words)
    print("Liczba liter: ", letters)
    print("Liczba cyfr: ", numbers)
    print("Liczba wystąpień poszczególnych znaków: ", usedCharacters)

main()
