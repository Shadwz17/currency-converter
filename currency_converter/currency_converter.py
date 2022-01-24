import conversion

option = 0
title = "Welcome to currency converter - by Shadwz"


while option == 0:
    print("\n" + title + "\n" + "-" * len(title) + "\n")
    option = int(input("Choose an option:\n"
          "1. Dollar to Euro\n"
          "2. Euro to Dollar\n"
          "3. Euro to Pound\n"
          "4. Pound to Euro\n"))

    if option == 1:
        amount_dollars = float(input("How much dollars to euros? "))

        amount_euro = conversion.dollar_to_euro(amount_dollars)
        print(f"The amount of {amount_dollars} dollars to euros is {round(amount_euro, 2)}")

    elif option == 2:
        amount_euro = float(input("How much euros to dollars? "))

        amount_dollars = conversion.euro_to_dollar(amount_euro)
        print(f"The amount of {amount_euro} euros to dollars is {round(amount_dollars, 2)}")

    elif option == 3:
        amount_euro = float(input("How much euros to pounds? "))

        amount_pounds = conversion.euro_to_pound(amount_euro)
        print(f"The amount of {amount_euro} euros to pound is {round(amount_pounds, 2)}")

    elif option == 4:
        amount_pounds = float(input("How much pounds to euros? "))

        amount_euro = conversion.pound_to_euro(amount_pounds)
        print(f"The amount of {amount_pounds} pounds to euros is {round(amount_euro, 2)}")

    else:
        print(f"Wrong! {option} is not an option")
        exit()
