#define the function needed, add, sub, mul, div
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

#print options to the user
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

#ask for values
choice = input("input your choice")

#loop to continue the program until the user wants to exit
if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    #call the functions
    add(a, b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    mul(a, b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    div(a, b)
elif choice == "e" or choice == "E":
    print("program ended")
    quit()
