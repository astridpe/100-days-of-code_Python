from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while coffee_machine_on:

    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    items = menu.get_items()
    user_choice = input(f"What would you like? ({items}): ")

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        coffee_machine_on = False

    # TODO 3. Print report.
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)

        # TODO 4. Check resources sufficient?
        if coffee_machine.is_resource_sufficient(drink):

            # TODO 5. Check transaction successful?
            if money_machine.make_payment(drink.cost):

                # TODO 6. Make Coffee:
                coffee_machine.make_coffee(drink)

















