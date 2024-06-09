from decimal import Decimal

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = user_input(menu)
    print ("\n")

def user_input(menu):
    total = Decimal(0.00)
    while True:
        try:
            food_item = input("Item: ").title()
            if food_item in menu:
                total = total + Decimal(menu[food_item])
                print(f"${total:.2f}")
        except EOFError:
            return total

main()
