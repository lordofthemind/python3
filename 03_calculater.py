def add(a, b):
    answer = a+ b
    print(str(a) + " + " + str(b) +"=" + str(answer))

def sub(a, b):
    answer = a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))
    
def mul(a, b):
    answer =a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
    answer =a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a= int(input("input first number: "))
        b= int(input("input Second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("You Choose Multiply and conqure: ")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("You choose Divide and conqure!")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Programm Ended!!!")
        quit()