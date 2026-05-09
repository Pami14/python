import csv
import os

FILE_NAME = "inventory.csv"
FIELD_NAMES = ["name", "quantity", "category"]

# inventory ["name": "soldering iron", "quantity": 2, "category": "electronics"]
inventory = []

def add_to_inventory():
    new_name = input("What do you want to add? ")
    
    existing_item = next((item for item in inventory if item["name"].lower() == new_name.lower()), None)

    if existing_item:
        while True:
            try: 
                new_pieces = int(input("How many more to add to inventory? "))
                existing_item["quantity"] += new_pieces
                break
            except ValueError:
                print("Enter value for pieces.")
    else:
        cat = input("Wich category is item? ")
        
        while True:
            try:
                pieces = int(input("How many pieces do you want to add? "))
                entry = {"name": new_name, "quantity": pieces, "category": cat}
                inventory.append(entry)
                break
            except ValueError:
                print("Enter value for pieces.")

    # ----- INFO -----
    # if not any(name["name"].lower() == new_name for name in inventory):
    # -> this approach would only find if it is exiting and i would have to look for the index again!!
    # for index, item in enumerate(inventory):
    #     if item["name"] == new_name:
    #         found_index = index
    #         break 
    # inventory[found_index]["quantity"] += pieces
       
def is_inventory_empty():
    if not inventory:
        print("Inventory is empty!")
        return True
    return False

def list_inventory():
    if not is_inventory_empty():
        for i, entry in enumerate(inventory, start= 1):
            print(f"{i}. name: {entry['name']:<15} quantity: {entry['quantity']:<3} category: {entry['category']:<15}")

def take_out_inventory():
    name = input("Enter item name: ")
    found_item = next((item for item in inventory if item["name"].lower() == name.lower()), None)

    if found_item:
        while True:
            pieces = int(input("How many pieces to take out? "))
            try:
                if found_item["quantity"] < pieces:
                    raise ValueError(f"For the selected item {found_item['name']} only {found_item['quantity']} pieces are in inventory!")
                found_item["quantity"] -= pieces
                break
            except ValueError as e:
                print(f"Invalide number: {e}")
    else:
        print(f"{name} doesn't exist in inventory!")

def store_to_file():
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(inventory)

def read_from_file():
    if not os.path.exists(FILE_NAME):
        return[]
    
    loaded_data = []
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            loaded_data.append(row)
    return loaded_data

# -----  Start Program  -----

inventory = read_from_file()

while True:
    print("\nChoose Option for Inventory:")
    print("\n1. add item")
    print("\n2. list all items")
    print("\n3. take out from inventory")
    print("\n5. exit")
    select = input("\nChoose option: ")

    if select == "1":
        add_to_inventory()
        store_to_file()

    elif select == "2":
        list_inventory()

    elif select == "3":
        take_out_inventory()
        store_to_file()
    
    elif select == "5":
        break

