from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_running = True
while is_running:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        is_running = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_choice)
        if menu_item:
            if coffee_maker.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)