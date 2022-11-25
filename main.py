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
#TODO 0: ask
to_make = input("what would you like? (espresso/latte/cappuccino): ")

 #TODO:1 print report.
if to_make == "report":
    for res in resources:
        print(f"{res}:{resources[res]}")

# TODO 2:check resources sufficent?
def resources_check():
    if to_make == 'espresso':
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] or  resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("sorry insufficient resources")
    if to_make == 'latte':
        if resources["water"] < MENU["latte"]["ingredients"]["water"] or  resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("sorry insufficient resources")
    if to_make == 'cappuccino':
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("sorry insufficent resources")
resources_check()




#TODO 3:process coins.
print("plese insert coin.")
quarters = 0.25 * int(input("how many quarters?"))
dimes = 0.10 * int(input("how many dimes?"))
nickles = 0.05 * int(input("how many nickles?"))
pennies = 0.01 * int(input("how many pennies?"))
total = quarters + dimes + nickles + pennies





#TODO 4 :check trasaction successfully
if to_make == "espresso":
    cost = 1.5
if to_make == "latte":
    cost = 2.5
if to_make == "cappuccino":
    cost = 3.0
r_money = total - cost
if r_money < 0:
    print("sorry thats not enough money? money has been refunded")
else:
    print(f"here is your {r_money}")
    print( f"here is ur {to_make}. enjoy!")




#TODO 5:make cofee