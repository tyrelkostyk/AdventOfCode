import csv

decimalZero = ord('0')
decimalNine = ord('9')

firstDigit = 0
secondDigit = 0

rowValue = 0
sumValue = 0

fiveNumber = 5
anotherNumber = 50302
fiveString = "5"
anotherString = "Hello"


# Open the CSV file
with open('inputs.csv', 'r') as file:
    # Create a CSV reader
    csvReader = csv.reader(file)

    # Iterate through the rows
    for row in csvReader:
        for char in ''.join(row):
            if ord(char) >= decimalZero and ord(char) <= decimalNine:
                firstDigit = char
                break

        for char in ''.join(row)[::-1]:
            if ord(char) >= decimalZero and ord(char) <= decimalNine:
                secondDigit = char
                break

        rowValue = firstDigit + secondDigit
        sumValue += int(rowValue)
        print("Row Value: " + str(rowValue) + " New Sum: " + str(sumValue))

print("Final Sum: " + str(sumValue))

asdfasdf

