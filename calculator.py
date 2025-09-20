while True:
    try:

        choice=input("What operation do you want to perform \n" \
        "1.Addition\n" \
        "2.Subtraction \n" \
        "3.Multiplication \n" \
        "4.Division \n"  \
        "5.Exit \n").lower()

        if choice == "exit" or choice == "5":
            print("exiting the calculator....GoodBye !")
            break

        num1 = int(input("Enter the value of Number 1: "))
        num2 = int(input("Enter the value of Number 2: "))

        match choice:
            case "addition" | "1":
                print(f"Addition: {num1} + {num2} = {num1 + num2}")
            case "subtraction" | "2":
                print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
            case "multiplication" | "3":
                print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
            case "division" | "4":
                if(num2 == 0):
                    print("Divisible by Zero Error...")
                else:
                    print(f"Division: {num1} / {num2} = {num1 / num2}")
            case _:
                print("Invalid choice, Please try again...")

    except ValueError:
        print("Invalid value, Please enter numbers only...")