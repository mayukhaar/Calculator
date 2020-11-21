print("BASIC CALCULATOR")
print(".................")
print("These are instructions on how to use this calculator ")
print("                     ")

repeat = "Y"


while repeat == "Y" or repeat == "y":

    op = input("Enter operation (+,-,*,/,^): ")
    if op != "+" or op != "-" or op != "*" or op != "/" or op != "^":
        print("Invalid operation.")
        op = input("Enter operation (+,-,*,/,^): ")
    num_1 = float(input( "Enter a number: "))
    num_2 = float(input("Enter another number: "))
    if op == "+":
        add = float(num_1) + float(num_2)
        print("Answer: " + str(add))
        repeat = input("Do you want to enter another calculation (Y/N): ")
    elif op == "-":
        subtract = float(num_1) - float(num_2)
        print("Answer: " + str(subtract))
        repeat = input("Do you want to enter another calculation (Y/N): ")
    elif op == "*":
        multiply = float(num_1) * float(num_2)
        print("Answer: " + str(multiply))
        repeat = input("Do you want to enter another calculation (Y/N): ")
    elif op == "/":
        divide = float(num_1) / float(num_2)
        print("Answer: " + str(divide))
        repeat = input("Do you want to enter another calculation (Y/N): ")
    elif op == "^":
        power = float(num_1) ** float(num_2)
        print("Answer: " + str(power))
        repeat = input("Do you want to enter another calculation (Y/N): ")
    else:
        print("Invalid operation.")


print("Bye! Have a nice day:)")

#repeat = input("Do you want to enter another calculation (Y/N: ")


#else:
#print("jdhsf")
    #if repeat == "N":
       # print("Bye! Have a nice day :)")
    #else:
      #  print ("Invalid operation.")
      #  print(repeat)




