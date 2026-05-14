# Importing tabulate module
from tabulate import tabulate

# Vending Machine Data
vending_machine = {
    "Snacks": {
        "S01": {"name": "Lays Chips", "price": 1.00, "stock": 9},
        "S02": {"name": "Terra", "price": 2.50, "stock": 11},
        "S03": {"name": "Popchips", "price": 2.00, "stock": 15},
        "S04": {"name": "Doritos", "price": 2.25, "stock": 18},
        "S05": {"name": "Ruffles", "price": 2.75, "stock": 30},
        "S06": {"name": "Fritos", "price": 3.65, "stock": 13},
        "S07": {"name": "Cheetos", "price": 3.00, "stock": 14},
    },
    "Drinks": {
        "D01": {"name": "Sprite", "price": 1.75, "stock": 13},
        "D02": {"name": "Mountain Dew", "price": 1.75, "stock": 12},
        "D03": {"name": "Seven Up", "price": 2.25, "stock": 12},
        "D04": {"name": "Cola Diet", "price": 2.50, "stock": 11},
        "D05": {"name": "Cola Regular", "price": 1.75, "stock": 14},
        "D06": {"name": "Fanta", "price": 3.75, "stock": 15},
        "D07": {"name": "Starbucks", "price": 4.55, "stock": 14},
        "D08": {"name": "Water", "price": 1.75, "stock": 12},
    },
    "Chocolates": {
        "C01": {"name": "Dairy Milk", "price": 5.65, "stock": 11},
        "C02": {"name": "Toblerone", "price": 4.75, "stock": 15},
        "C03": {"name": "Kinder Bars", "price": 1.50, "stock": 13},
        "C04": {"name": "Dark Chocolate Bar", "price": 5.50, "stock": 19},
        "C05": {"name": "Twix", "price": 1.75, "stock": 20},
        "C06": {"name": "Snickers", "price": 2.75, "stock": 11},
        "C07": {"name": "Cadbury", "price": 5.75, "stock": 15},
        "C08": {"name": "Godiva Chocolatier", "price": 6.75, "stock": 16},
    }
}

# Display Menu Function
def display_menu(category=None):
    table = []

    if category:
        for code, item in vending_machine[category].items():
            stock = item["stock"] if item["stock"] > 0 else "Out of stock"
            table.append([code, item["name"], f"${item['price']:.2f}", stock])
        return tabulate(table, headers=["Code", "Item", "Price", "Stock"], tablefmt="pretty")

    else:
        categories = list(vending_machine.keys())
        for i, cat in enumerate(categories, start=1):
            table.append([i, cat])
        return tabulate(table, headers=["Code", "Category"], tablefmt="pretty")


# Main Program
def main():
    print("=== Welcome to the Vending Machine ===")

    total_cost = 0
    purchased_items = []
    categories = list(vending_machine.keys())

    while True:
        print("\nCategories")
        print(display_menu())

        choice = input("Choose category code (or 'done'): ").strip().lower()

        if choice == "done":
            break

        if not choice.isdigit() or not (1 <= int(choice) <= len(categories)):
            print("Invalid category code.")
            continue

        category = categories[int(choice) - 1]
        print(f"\n--- {category} Menu ---")
        print(display_menu(category))

        item_code = input("Enter item code (or 'back'): ").strip().upper()

        if item_code == "BACK":
            continue

        item = vending_machine[category].get(item_code)
        if not item:
            print("Invalid item code.")
            continue

        if item["stock"] <= 0:
            print("Item is out of stock.")
            continue

        # Quantity
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0 or qty > item["stock"]:
                print("Invalid quantity.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        cost = item["price"] * qty
        total_cost += cost
        item["stock"] -= qty
        purchased_items.append(f"{item['name']} x{qty}")

        print(f"Added successfully. Current total: ${total_cost:.2f}")

    # Payment
    if total_cost > 0:
        print("\nPurchased Items:")
        for p in purchased_items:
            print("-", p)

        print(f"\nTotal to pay: ${total_cost:.2f}")

        paid = 0
        while paid < total_cost:
            try:
                payment = float(input("Insert money: $"))
                paid += payment
                print(f"Paid so far: ${paid:.2f}")
            except ValueError:
                print("Invalid amount.")

        change = paid - total_cost
        print(f"\nPayment successful! Change: ${change:.2f}")

    else:
        print("No items purchased.")

    print("\nThank you for using the Vending Machine!")


# Run Program
if __name__ == "__main__":
    main()
