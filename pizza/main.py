# pizza sizes and prices
small = 100.00
medium = 125.00
large = 150.00
family = 200.00

# sides and prices
small_pepperoni = 20.00
medium_large = 40.00
family_pepperoni = 50.00
cheese = 20.00

# total bill 
total_bill = 0.00

def small_pizza():
        total_bill = small
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += small_pepperoni
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"\nTotal bill is Ghc{total_bill}\n")

def medium_pizza():
        total_bill = medium
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += medium_large
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"\nTotal bill is Ghc{total_bill}\n")

def large_pizza():
        total_bill = large
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += medium_large
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"\nTotal bill is Ghc{total_bill}\n")

def family_pizza():
        total_bill = family
        add_pepperoni = input("Would you add extra pepperoni?[y/n]\n").lower()
        if add_pepperoni == 'y':
            total_bill += family_pepperoni
        extra_cheese = input("Would you add and extra cheese?[y/n]\n").lower()
        if extra_cheese == 'y':
            total_bill += cheese
        print(f"\nTotal bill is Ghc{total_bill}\n")
# infinite loop
while True:
    print("**Welcome To Pizza Palace**")
    
    try:
        menu_choice = input("s for small\n" 
                    "m for medium\n"
                    "l for large\n" 
                    "f for family\n"
                    "e to exit the program\n"
                    "\nPlease select your choice?: ").lower()

        if menu_choice == 's':
            small_pizza()
        elif menu_choice == 'm':
            medium_pizza()
        elif menu_choice == 'l':
            large_pizza()
        elif menu_choice == 'f':
            family_pizza()
        elif menu_choice == "e":
            print("\n**Closing Program**\n")
            exit()
        else:
            print("\nKindly provide an option from the manu!!!.\n")
    except ValueError:
        print("\nKindly enter a valid value\n")