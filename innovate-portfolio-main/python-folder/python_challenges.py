
#! Activity One
# Create variable that holds the text “Welcome to Code Nation”. Find the length of the string and save this to a new variable.
# Create a function that checks if the string length is even; if it is, print the string, the length and an appropriate message in one sentence. Do the same but with a different message if it’s odd.
# Change the string length so you can test all possible outcomes

def check_length():
    var = "Welcome to Code Nation"
    var_length = len(var)

    if var_length % 2 == 0:
        print(f"The length of [{var}] is {var_length} and it is EVEN!")
    else:
        print(f"The length of [{var}] is {var_length} and it is ODD!")
check_length()

#! Activity Two
# Create a list that represents the alphabet: alphabet = ["a", "b", "c", "d"...
# Create a for loop to iterate through this and print each letter in order
# Now using input, allow the user to type a number and print the letter it represents in the alphabet.
# Remember how index works - and think about how to structure your code.

alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]
# for i in alphabet:
#     print(i)

def check_alphabet():
    number = input("Please select a number between 1 and 26.\n")
    number = int(number)
    number = (number - 1)
    print(f"Your letter is {alphabet[number]}")
check_alphabet()