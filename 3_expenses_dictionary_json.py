import json

FILE_NAME = "expenses.json"

# A list to hold dictionaries: [{"item": "Coffee", "price": 5.50},...]
expenses = []

def save_data():
    # w = write mode
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)
    print("Disk updated")

def open_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # file doesn't exist yet
        return[]
    
def add_expenses():
    name = input("What did you buy? ")

    while True:
        try:
            price = float(input("How much did it cost? "))
            # -> Dictionary
            entry = {"item": name, "price": price}
            expenses.append(entry)
            save_data()
            break
        except ValueError:
            print("Invalid price. Enter number.")

def show_total():
    total = sum(item["price"] for item in expenses)
    print(f"\n--- Total Spent: €{total:.2f} ---")    

def is_list_empty():
    if not expenses: # emtpy check
        print("No expenses recorded yet.")
        return True
    return False

# def is_item_in_list():
#     search = input("Which item are you looking for?")

#     for i, entry in enumerate(expenses):
#         if entry["item"] == search:
#             return True
#     return False

# def is_item_in_list():
#     search = input("Which item?").lower()
#     return any(item["item"].lower() == search for item in expenses)

def find_how_often_item_in_list():
    search = input("Which item?").lower()

    price = [entry["price"] for entry in expenses if entry["item"].lower() == search]

    count = len(price)
    total_item_price = sum(price)

    print(f"{search} found {count} in list. Total €{total_item_price:.2f}")


expenses = open_data()

while True:
    print("\n--- Options: ---")
    print("\n1. add a new item")
    print("\n2. show all items")
    print("\n3. calculate total")
    print("\n4. calculate total")
    print("\n5. exit")

    selection = input("\nChoos a number: ").strip() #remobe accidental spaces at the start/end " 1" or "1 "
    
    if selection == "1":
        add_expenses()

    elif selection == "2":
        if not is_list_empty():
            for i, entry in enumerate(expenses):
                # name = entry["item"]
                # cost = entry["price"]
                # print(f"{i + 1}.{name}: €{cost:.2f}")
                # print(f"{i + 1}.{entry["item"]}: €{entry["price"]:.21f}")
                print(f"{i + 1}.{entry['item']:<15} | €{entry['price']:>8.2f}")

    elif selection == "3":
        if not is_list_empty():
            show_total()

    elif selection == "4":
        if not is_list_empty():
            find_how_often_item_in_list()

    elif selection == "5":
        break
    
    else:
        print("invalide input.")