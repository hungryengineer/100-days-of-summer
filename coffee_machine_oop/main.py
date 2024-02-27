from cofee_machine_data import MENU, resources
from resource_checker import ResourceChecker
from coffee_dispenser import CoffeeDispenser

current_resources = ResourceChecker(resources) #object declared from class
print(f"current resources are:\n{current_resources.resources['water']}\n{current_resources.resources['milk']}\n{current_resources.resources['coffee']}")

dispenser = CoffeeDispenser(1,2,3)
choice = input("which coffee do you want?\ntype 1 for espresso\ntype 2 for latte\ntype 3 for cappuccino\n")
if choice == "1":
    print(f"dispensing espresso {MENU['espresso']['ingredients']}")
