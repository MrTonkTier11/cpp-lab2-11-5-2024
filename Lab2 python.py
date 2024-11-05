import time
"""Write a code that performs addition, subtraction, multiplication and 
division to any 2 numbers given by the user. Display each result individually"""
def arithOperation():
    num_one = float(input("Please enter your first number: "))
    num_two = float(input("Please enter your second number: "))

    addition = num_one + num_two
    subtraction = num_one - num_two
    multiplication = num_one * num_two
    division = num_one / num_two

    print("When your two numbers are added, the result is: " + str(addition) + "\nWhen your two numbers are subtracted, the result is:  " + str(subtraction) + 
        "\nWhen your two numbers are multiplied, the result is:  " + str(multiplication) + "\nWhen your two numbers are divided, the result is:  " + str(division))
    

"""Write a code that asks the user for the name and section"""
def name_and_section():
    name = input("Please enter your name: ")
    section = input("Please enter your section: ")
    print("Name: " + name + "\nSection: " + section)

#main code (comment lang ito pero nilagyan ko ng main kasi kalat sa python maglagay)
while True:
    choice_one = input("choose which one would you like to start: \na.)Arithmetic Operations \tb.)Name & Section \n")

    #pag letter a pinili
    if choice_one == 'a':
        arithOperation()

    #oag ketter b pinili
    elif choice_one == 'b':
        name_and_section()

    #kung gusto umulit sa simula
    loopChoice = input("Would you like to try again? \nYes or No: ")

    if loopChoice.lower() == "yes":
        continue
    else:
        print("will end in 3")
        time.sleep(1)
        print("will end in 2")
        time.sleep(1)
        print("will end in 1...")
        time.sleep(1)
        break