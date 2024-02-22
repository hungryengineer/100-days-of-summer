from cofee_machine_data import MENU,resources
#print(resources)#code check
cost_of_espresso = MENU['espresso']['cost']
cost_of_latte = MENU['latte']['cost']
cost_of_cappuccino = MENU['cappuccino']['cost']

##check if resources are sufficient
def resource_checker(water,milk,coffee):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return water,milk,coffee
resource_checker('water','milk','coffee')

##make coffee
##process coins
def coffee():
    choice = input("which coffee do you want?\ntype 1 for espresso\ntype 2 for latte\ntype 3 for cappuccino\n")
    if choice == "1":
        print(f"dispensing espresso {MENU['espresso']}")
        print(f"current resources are: {resource_checker('water','milk','coffee')}")
        print(f"please pay ${cost_of_espresso}\ninsert {cost_of_espresso/0.25} quarters")
        quarters = float(input("Please enter the number of quarters\n"))
        if quarters == (cost_of_espresso/0.25):
            print("be ready, dispensing!")
        else:
            print("Wrong amount detected! retry.")
            coffee()

    elif choice == "2":
        print(f"dispensing latte {MENU['latte']}")
        print(f"current resources are: {resource_checker('water', 'milk', 'coffee')}")
        print(f"please pay ${cost_of_latte}\ninsert {cost_of_latte / 0.25} quarters")
        quarters = float(input("Please enter the number of quarters\n"))
        if quarters == (cost_of_latte / 0.25):
            print("be ready, dispensing!")
        else:
            print("Wrong amount detected! retry.")
            coffee()

    elif choice == "3":
        print(f"dispensing cappuccino {MENU['cappuccino']}")
        print(f"current resources are: {resource_checker('water', 'milk', 'coffee')}")
        print(f"please pay ${cost_of_cappuccino}\ninsert {cost_of_cappuccino / 0.25} quarters")
        quarters = float(input("Please enter the number of quarters\n"))
        if quarters == (cost_of_cappuccino / 0.25):
            print("be ready, dispensing!")
        else:
            print("Wrong amount detected! retry.")
            coffee()
coffee()

