from main import MENU, resources


def coffee_machine_resources():
    """Generate the current resource values in the coffee machine"""
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}g")
    print(f"Money : ${money}")


def coffee_required_resources():
    """Generate the required resource values for espresso, latte and cappuccino"""
    if user_coffee == "espresso":
        espresso_water = MENU["espresso"]["ingredients"]["water"]
        espresso_milk = 0
        espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
        espresso_cost = MENU["espresso"]["cost"]
        return espresso_water, espresso_milk, espresso_coffee, espresso_cost

    elif user_coffee == "latte":
        latte_water = MENU["latte"]["ingredients"]["water"]
        latte_milk = MENU["latte"]["ingredients"]["milk"]
        latte_coffee = MENU["latte"]["ingredients"]["coffee"]
        latte_cost = MENU["latte"]["cost"]
        return latte_water, latte_milk, latte_coffee, latte_cost

    elif user_coffee == "cappuccino":
        cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
        cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
        cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cappuccino_cost = MENU["cappuccino"]["cost"]
        return cappuccino_water, cappuccino_milk, cappuccino_coffee, cappuccino_cost


def coin_payment():
    """Calculate the amount of coins the user has inserted into the coffee machine"""
    print("Please insert coins.")
    coin_inserted = int(input("How many $2: ")) * 2
    coin_inserted += int(input("How many $1: "))
    coin_inserted += int(input("How many $0.50: ")) * 0.5
    coin_inserted += int(input("How many $0.20: ")) * 0.2
    coin_inserted += int(input("How many $0.10: ")) * 0.1
    return coin_inserted


water, milk, coffee, money = resources["water"], resources["milk"], resources["coffee"], 0
coffee_machine_on = True

while coffee_machine_on:
    user_coffee = input("What would you like? (Espresso / Latte / Cappuccino)\n").lower()
    if user_coffee == "off":
        coffee_machine_on = False
    elif user_coffee == "report":
        coffee_machine_resources()
    else:
        coffee_required_resources()
        required_water, required_milk, required_coffee, required_cost = coffee_required_resources()
        if water >= required_water and milk >= required_milk and coffee >= required_coffee:
            user_payment = coin_payment()
            if user_payment < required_cost:
                coffee_machine_on = False
                print(f"Sorry that's not enough money. $ {user_payment} refunded.")
            elif user_payment >= required_cost:
                user_balance = round(user_payment - required_cost, 2)
                money += required_cost
                water -= required_water
                milk -= required_milk
                coffee -= required_coffee
                print(f"The cost of {user_coffee} is $ {required_cost}.")
                print(f"Here is $ {user_balance} in change. Enjoy your {user_coffee} ☕!")

        elif water <= required_water:
            coffee_machine_on = False
            print("Sorry, there is not enough water.")

        elif milk <= required_milk:
            coffee_machine_on = False
            print("Sorry, there is not enough milk.")

        elif coffee <= required_coffee:
            coffee_machine_on = False
            print("Sorry, there is not enough coffee.")
