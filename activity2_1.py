input = input("enter a number into the terminal:")
try: 
 int(input) != input
 print("number is integer")
except:
 print("\n ERROR: please input only numerical values. \n")
 print("**************************** \n")