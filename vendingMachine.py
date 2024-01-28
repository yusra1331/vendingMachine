#Create drinks and its price
drinks = {
    '1': {'drink': 'Cola', 'price': 1.35},
    '2': {'drink': 'Coffee', 'price': 2.70},
    '3': {'drink': 'Soda', 'price': 1.20},
    '4': {'drink': 'Water', 'price': 1.00}
}

def DisplayMenu(): #for display
    
    print("Welcome to YUSRA Vending Machine!")
    print("Here the drinks that available:")

    for key, drink in drinks.items():
        print(f"{key}. {drink['drink']} - RM{drink['price']}")

def PurchaseDrinks(): #select one or more drinks
    TotalAmountDue = 0.0
    SelectedDrinks = []

    while True:
        selection = input("Enter the drink number you wish to purchase (or 'done' to finish): ")

        if selection.lower() == 'done':
            break
        elif selection in drinks:
            SelectedDrink = drinks[selection]
            SelectedDrinks.append(SelectedDrink)
            TotalAmountDue += SelectedDrink['price']
        else:
            print("Invalid selection. Please try again.")

    return SelectedDrinks, TotalAmountDue

def MakePayment(AmountDue): #making payment
    while AmountDue > 0:
        try:
            payment = float(input(f"Please insert RM{AmountDue:.2f}: "))
            if payment >= AmountDue:
                change = payment - AmountDue
                print(f"Thank you for your purchase! Your change is RM{change:.2f}.")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                AmountDue -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
#main code
DisplayMenu()
SelectedDrinks, TotalAmountDue = PurchaseDrinks()

if SelectedDrinks:
    print("\n\nYou have selected the following drinks:")
    for drink in SelectedDrinks:
        print(f"{drink['drink']} - RM{drink['price']:.2f}")

    print(f"\nTotal amount due: RM{TotalAmountDue:.2f}")
    MakePayment(TotalAmountDue)
else:
    print("\nNo drinks selected. It's okay")
