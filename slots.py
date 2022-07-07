from random import choice

def randomize():
    wheeloptions = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "SEVEN"] 
    return choice(wheeloptions)

again = "yes"
while again == "yes":
    input("PRESS 1 TO ROLL:")

    first_wheel = randomize()
    second_wheel = randomize()
    third_wheel = randomize()

    print(first_wheel)
    print(second_wheel)
    print(third_wheel)
    
    if first_wheel == second_wheel and first_wheel == third_wheel: print("CONGRATULATIONS YOU WON THE JACKPOT")

    elif first_wheel == second_wheel or first_wheel == third_wheel or second_wheel == third_wheel: print("Close, but not there yet")

    else: print("Too bad, try again")
    again = input("Do you want to try again, yes/no?")
    