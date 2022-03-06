MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


# TODO 4. Check resources sufficient. Make a function that checks if there are enough resources to make the drink.
def check_resources(order_ingredients):
    """Returns True when order can be made and False if ingrediens are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# TODO 5. If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# TODO 6. Process coins. Make a function that calculate the monetary value of the coins inserted.
#  E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def is_transaction_successful(money_recevied, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recevied >= drink_cost:
        change = round(money_recevied - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 7. If the transaction is successful and there are enough resources to make the drink the user selected,
#  then the ingredients to make the drink should be deducted from the coffee machine resources.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



# TODO 1b. The prompt should show again after a task is completed to serve the next costumer (make a loop)
coffee_machine_on = True
profit = 0

while coffee_machine_on:
    # TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        coffee_machine_on = False

    # TODO 3. Print report.
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    # TODO 1a. Check users choice
    else:
        drink = MENU[user_choice]

        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])




