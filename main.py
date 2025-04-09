# This code is for coffee machine. You have 3 options. Espresso,latte and cappuccino. Every time a drink is selected, the machine should check
# if we have enough ingredients to make the drink. You can find out the amount of ingredients left by typing report in the "What would you like to do question"
# you can close the machine by typing off in "What would you like to do question"
# you can close the machine by typing espresso/latte/cappuccino in "What would you like to do question"
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def making_a_drink():
    should_continue = True

    while should_continue:
        action = input("What would you like? (espresso/latte/cappuccino or report to find out the amount of ingredients or off to turn off the machine): \n").lower()
        if action != "off" and action != "report" and action != "espresso" and action != "latte" and action!= "cappuccino":
            print("wrong selection. Please try again")

        elif action == "report":
            print(f"Remaining quantity of : \n- Water: {resources["water"]}ml \n- Milk: {resources["milk"]}ml \n- Coffee: {resources["coffee"]}ml")



            # for key, value in resources.items():
            #     print("remaining quantity of" ,key, ":", value)

            should_continue = False

        elif action == "off":
            print("\n" * 20)

            should_continue = False

        elif action == "espresso" or action == "latte" or action == "cappuccino":
            print(f" To make your drink, you need : \n - {MENU[action]["ingredients"]["water"]}ml of water \n - {MENU[action]["ingredients"]["coffee"]}ml of coffee \n - {MENU[action]["ingredients"]["milk"]}ml of milk")

# This cod compares the amount of ingredients required to make the drink with the amount of ingredients left. If we do not have enough ingredient
# to make the drink then the code should stop and tell the customer  which ingredient the coffee machine does not have enough of.
            if MENU[action]["ingredients"]["water"] <= resources["water"]:
                if MENU[action]["ingredients"]["coffee"] <= resources["coffee"]:
                    if MENU[action]["ingredients"]["milk"] <= resources["milk"]:
                        budget = input(f"The price of your {action} is {MENU[action]["cost"]}$. Do you have enough money to by your {action}?Type 'yes' or 'No'\n").lower()
                        if budget == "no":
                            print("Sorry you do not have enough.Hope to see you next time")
                            print("\n" * 20)

                            should_continue = False
                        else:
                            pennies = int(input("How many pennies did you insert?: "))
                            nickels = int(input("How many nickels did you insert?: "))
                            dimes = int(input("How many dimes did you insert?: "))
                            quarters = int(input("How many quarters did you insert?: "))

                            def total_coins_inserted(coin1, coin2, coin3, coin4):
                                total_money = (0.01 * coin1 + 0.05 * coin2 + 0.1 * coin3 + 0.25 * coin4)
                                return total_money
                            if total_coins_inserted(pennies, nickels, dimes, quarters) >= MENU[action]["cost"]:
                                resources["water"] -= MENU[action]["ingredients"]["water"]
                                resources["coffee"] -= MENU[action]["ingredients"]["coffee"]
                                resources["milk"] -= MENU[action]["ingredients"]["milk"]
                                change = round((total_coins_inserted(pennies, nickels, dimes, quarters) - MENU[action]["cost"]),2)
                                print(f"Here is your {action}. Enjoy! Your change is {change}")
                                print(f" remaining water {resources['water']}")
                                print(f" remaining coffee {resources['coffee']}")
                                print(f" remaining milk {resources['milk']}")
                            else:
                                print("Sorry!You don't have enough money for your latte. Money refunded")
                                should_continue = False
                    else:
                        print("Sorry!You don't have enough milk for your latte. Money refunded")
                        should_continue = False
                else:
                    print("Sorry!You don't have enough coffee for your latte. Money refunded")
                    should_continue = False
            else:
                print("Sorry! You don't have enough water for your latte. Money refunded")
                should_continue = False

making_a_drink()

