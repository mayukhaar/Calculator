print("Basic Calculator")
print(".................")
num_1 = float(input( "Enter a number: "))
op = input("Enter operation: ")
num_2 = float(input("Enter another number: "))

if op == "+":
    print(float(num_1) + float(num_2))
elif op == "-":
    print(float(num_1) - float(num_2))
elif op == "*":
    print(float(num_1) * float(num_2))
elif op == "/":
    print(float(num_1) / float(num_2))
else:
    print("Invalid operation.")



#result = float(num_1) + float(num_2)
#print("Answer: " + str(result))


