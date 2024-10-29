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
def truncate (number, decimal_places):
    factor = 10 ** decimal_places
    return int(number * factor) / factor
def coffee_cost (price, current_money):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dime?: "))
    nickle = int(input("how many nickle?: "))
    pennies = int(input("how many pennies?: "))
    quarters = float(.25 * quarters)
    dimes = float(.10 * dimes)
    nickle = float(.05 * nickle)
    pennies = float(.01 * pennies)
    inserted_coins = float(quarters + dimes + nickle + pennies)
    if inserted_coins >= price:
        vendor_money = price
        current_money += vendor_money
        change = inserted_coins - price
        my_change = truncate(change, 2)
        current_money = truncate(current_money, 2)
        return (my_change, current_money)
    else:
        print("Sorry that's not enough money. Money refunded.")
def coffee(drink, current_money):
    drink_ingredients = MENU[drink]
    drink_cost = MENU[drink]["cost"]
    resource_water = resources['water']
    resource_milk = resources['milk']
    resource_coffe = resources['coffee']
    drink_water = (drink_ingredients['ingredients']['water'])
    if drink == 'latte'or drink == 'cappuccino':
        drink_milk = (drink_ingredients['ingredients']['milk'])
    else:
        drink_milk = 0
    drink_coffe = (drink_ingredients['ingredients']['coffee'])
    if drink_water <= resource_water and drink_milk <= resource_milk and drink_coffe <= resource_coffe:
        resources['water'] = resources['water'] - drink_water
        resources['milk'] = resources['milk'] - drink_milk
        resources['coffee'] = resources['coffee'] - drink_coffe

        my_change, current_money = coffee_cost(drink_cost, current_money)
        if my_change > 0:
            print(f"Here is your change ${my_change}.")
            print(f"Here is your {drink}. Enjoy!")
            return current_money
        elif my_change == 0:
            print(f"Thanks for your order")
def report(total_money):
    resourses_left = resources
    for items in resourses_left:
        print(f"{items}: {resourses_left[items]}")
        print(f"Money: ${total_money}")



make_drink = True
money = 0
#TODO: 1. create a user prompt, for what they like
while make_drink:
    input_data = input("What would you like? (espresso/latte/cappuccino): ")
    #TODO: 2. Create a funtion to to pick user selected drink
    if input_data == 'espresso' or input_data == 'latte' or input_data == 'cappuccino':
        current_money = coffee(input_data, money)
        try:
            money += current_money
        except TypeError:
            print('Out of drink resources')
            make_drink = False

    elif input_data == 'report':
        report(money)
    elif input_data == 'off':
        make_drink = False
    else:
        print("Invalid input")

#TODO: 3, create a funtion to print a report of the resourses
#TODO: 4, create a funtion to check id the resourses are suffient
#TODO: 5, promot user to inset coins
#TODO: 6, create a funtionion that calculaters the inserted coins, compare againgts cost and returns change
#TODO: 7, create a funtion thaa makes the coffe