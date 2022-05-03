def getUserInput():
    num1, num2 = None, None
    is_input = False

    while is_input == False:
        try:
            num1 = int(input("Please enter the first number:  "))
            num2 = int(input("Please enter the second number:  "))
            is_input = True
        except Exception as e:
            print("\nError, Please enter only number.\n\n")
    num_sub = num1 - num2
    num_sum = num1 + num2
    num_mul = num1 * num2
    num_pow = num1**num2
    num_div = num1 / num2 if num2 != 0 else 0

    print("\n**OPERATIONS ON YOUR NUMBERS**\n")

    print("substraction= " + str(num_sub))
    print("summation= " + str(num_sum))
    print("multiply= " + str(num_mul))
    print("power= " + str(num_pow))
    print("division= " + str(num_div))

    print()


if __name__ == "__main__":
    getUserInput()
