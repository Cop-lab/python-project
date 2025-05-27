# pizza sizes and prices
small = 100.00
medium = 125.00
large = 150.00
family = 200.00

# sides and prices
small_pepperoni = 20
medium_large = 40
family_pepperoni = 50
cheese = 20

total_bill = 0

print("***Welcome To Pizza Palace***")
menu_choice = input("Enter the size you want:\n" 
                    "s for small\n" 
                    "m for medium\n"
                    "l for large\n" 
                    "f for family:\n").lower()

try:
    if menu_choice == 's':
        total_bill += small
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += small_pepperoni
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    elif menu_choice == 'm':
        total_bill += medium
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += medium_large
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    elif menu_choice == 'l':
        total_bill += large
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += medium_large
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    elif menu_choice == 'f':
        total_bill += family
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += family_pepperoni
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    else:
        print("Kindly provide an option from the manu!!!.")
except ValueError:
    print("Kindly enter a valid value")