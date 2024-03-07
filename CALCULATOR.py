def sum(num1,num2):
    sum = num1 + num2
    return sum


def sub(num1,num2):
    sub = num1 - num2
    return sub


def mul(num1,num2):
    mul = num1*num2
    return mul


def div(num1,num2):
    div = num1/num2
    return div


while True:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))

    choice = int(input("Enter the choice : \n0 for exiting\n1 for adding\n2 for subtracting\n3 for multiplying\n4 for dividing "))
    if choice == 1:
        x = sum(num1,num2)
    elif choice == 2:
        x = sub(num1,num2)
    elif choice == 3:
        x = mul(num1,num2)
    elif choice == 4:
        x = div(num1,num2)
    elif choice == 0:
        break
    
    else:
        print("wrong input, try again")

    print(f"The result is",x)


