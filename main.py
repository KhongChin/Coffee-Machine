from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()}) \n").lower()
    if user_choice == "off":
        coffee_machine_on = False
    elif user_choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        coffee_chosen = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(coffee_chosen):
            if money_machine.make_payment(coffee_chosen.cost):
                coffeemaker.make_coffee(coffee_chosen)




