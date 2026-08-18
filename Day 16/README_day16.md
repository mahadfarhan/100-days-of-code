# Day 16 — OOP Coffee Machine

A command-line coffee machine project built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This version uses object-oriented programming to separate the menu, coffee machine resources, payment handling, and program flow into distinct classes and modules.

## Features

- Displays the available drinks
- Accepts `espresso`, `latte`, or `cappuccino` orders
- Supports the hidden `off` command to shut down the machine
- Supports the `report` command to display:
  - Remaining water
  - Remaining milk
  - Remaining coffee
  - Current profit
- Checks whether enough ingredients are available before making a drink
- Processes quarters, dimes, nickels, and pennies
- Refunds the user when insufficient money is inserted
- Returns change when too much money is inserted
- Deducts ingredients after a successful purchase
- Updates machine profit after successful transactions
- Continues serving customers until the machine is turned off

## Project Structure

```text
Day 16/
├── main.py
├── menu.py
├── coffee_maker.py
├── money_machine.py
└── README.md
```

### `main.py`

Controls the main program flow and coordinates interactions between the menu, coffee maker, and money machine.

### `menu.py`

Contains the `MenuItem` and `Menu` classes, including drink names, prices, ingredient requirements, and menu lookup functionality.

### `coffee_maker.py`

Contains the `CoffeeMaker` class, which manages machine resources, checks ingredient availability, generates resource reports, and makes drinks.

### `money_machine.py`

Contains the `MoneyMachine` class, which processes coins, handles payments and refunds, calculates change, and tracks profit.

## Concepts Practiced

- Object-oriented programming
- Classes and objects
- Using multiple Python modules
- Method calls between objects
- Encapsulation of responsibilities
- Program flow and control logic
- Dictionaries
- Loops and conditionals
- User input
- Resource management
- Payment and transaction logic

## Program Flow

The program repeatedly asks the user what they would like to order.

If a valid drink is selected:

1. The machine checks whether enough ingredients are available.
2. The user is prompted to insert coins.
3. The payment is checked against the drink price.
4. Change is returned when necessary.
5. The required ingredients are deducted.
6. The drink is dispensed.
7. The program returns to the main prompt for the next customer.

The `report` command displays the current resources and profit, while `off` ends the program.

## Course Attribution

The project requirements, class structure, and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
