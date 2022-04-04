# list of alphabets
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

for i in alphabet :
    print (i)


def check_alphabet():
    number = input("Please select a number between 1 and 26.\n")
    number = int(number)
    number = (number - 1)
    print(f"Your letter is {alphabet[number]}")
check_alphabet()