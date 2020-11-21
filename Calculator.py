print("BASIC CALCULATOR")
print(".................")
print("Instructions:")
print("-Enter the operation first, then enter the values in the order you want ")
print("the calculator to solve them.")
print("-When doing operations with powers, enter the base number first, then "
      "input the exponential value")
print("as the second number the calculator asks you to enter.")
print("-Enjoy :)")
print(" ")

repeat = "Y"

while repeat == "Y" or repeat == "y":

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


