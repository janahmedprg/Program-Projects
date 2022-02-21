import re

"""
Debug the functions below.

The function is expected to return an INTEGER.
The function accepts STRING_ARRAY serialNumber as parameter.
"""

def countCounterfeit(serialNumber):
    numberLength = len(serialNumber)
    if (numberLength < 0 or numberLength > 100000):
        # input invalid
        return 0

    total = 0

    for number in serialNumber:
        x = value(number)
        total = total + x + int(value(number)*0.01)

    # totalTax = total * 0.01
    # totalMinusTaxRounded = int(total - totalTax)
    return total #totalMinusTaxRounded

def isUpperCaseAZ(character):
    return bool(re.match(r'[A-Z]', character))

def value(s):
    if len(s) < 10 or len(s) > 12:
        return 0

    # The first 3 characters are distinct uppercase English letters.
    first3CharactersArray = s[0:3]

    first3CharactersSet = set(first3CharactersArray)
    if len(first3CharactersSet) < len(first3CharactersArray):
        return 0

    for character in first3CharactersArray:
        if not isUpperCaseAZ(character):
            return 0

    # The next 4 characters represent the year the note was created and will always be between 1900 and 2019 inclusive.
    yearCreatedCharacters = s[3:7]
    try:
        yearCreatedNumber = int(yearCreatedCharacters)
    except ValueError as val_err:
        return 0
    if yearCreatedNumber < 1900 or yearCreatedNumber > 2019:
        return 0

    # The next characters represent the currency denomination and may be any one of {10, 20, 50, 100, 200, 500, 1000}.
    valueString = s[7:len(s)-1]
    possibleValues = ['10', '20', '50', '100', '200', '500', '1000'];
    if not valueString in possibleValues:
        return 0

    valueNumber = int(valueString)

    if not isUpperCaseAZ(s[len(s) - 1]):
        return 0

    return valueNumber

if __name__ == '__main__':

    a_file = open(r"D:\Users\janah\Desktop\Projects\Program-Projects\py projects\input002.txt")
    file_contents = a_file.read()
    serialNumber = file_contents.splitlines()

    result = countCounterfeit(serialNumber)

    print(result)
