def main():
    print("This programs add two numbers.")
    num1 : str = input("Enter First Number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter Second Number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The Total is " + str(total) + ".")


if __name__== '__main__':
    main()


