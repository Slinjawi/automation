try:
    menu = int(input(
        "Choose option: \n 1.Decimal to Binary \n 2. Binary to Decimal\n Option: "))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu == 1:
        decimal = int(input("Input your Decimal number:\nDecimal: "))
        print("Decimal: {} ".format(bin(decimal)[2:]))
    elif menu == 2:
        binary = input("Input your binary number:\n Binary: ")
        print("Decimal: {} ".format(int(binary, 2)))
except ValueError:
    print("Please choose a valid option")
