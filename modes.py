# a lot of this functionality is implemented in database.py. If you want to take a look in there I've left some comments for documentation
import databases # should import it unless there is another python module called databases I don't know about
import receipt_gen
import os

def staff():
    pass

def customer(account):
    bag = []
    running = True
    while running:
        os.system('cls')
        print(f"Welcome {account['username']} -------------------------------------------------------------------------------------")
        action = input("Please select an action: display the catalogue(c), search(s), add item to bag(a), remove item from bag(r), show bag(b), checkout/pay(p), quit(q)\n: ").casefold()

        match action:
            case 'q': running = False; continue
            case 'c': print(databases.stock); input("Press ENTER: "); continue
            case 's':
                stype = input("what type of search would you like to make: name(n), category(c)\n: ").casefold()
                search = input("Please enter your search: ")
                if stype == 'n': field = "Item"
                elif stype == 'c': field = "Category"
                else: input("Unrecognized search tye: "); continue
                result = databases.stock.search(field, search)
                for item in result:
                    print(item["Item"],item["Category"],f"£{item['Price']}", sep=", ")
                input("Press ENTER: "); continue
            case 'a': 
                search = input("Please enter the name of the item you wish to add: ")
                result = (databases.stock.search("Item", search))[0]
                quantity = int(input("Please enter the amount of that item you wish to add: "))
                exists = False
                for item in bag:
                    if item["Item"] == result:
                        item["Quantity"] += quantity
                        exists = True
                        break
                if not exists: bag.append({"Quantity":quantity,"Item":result})
                print("Item added to bag")
                input("Press ENTER: "); continue
            case 'r':
                print("bag: ")
                for i, item in enumerate(bag):
                    print(f"\t{i}: {str(item['Quantity'])}x\t{item['Item']['Item']}\t£{int(item['Item']['Price'])*item['Quantity']}")
                index = int(input("please enter the id of the item you wish to remove: "))
                if index >= 0 and index < len(bag):
                    amount = int(input("how many of that item do you wish to remove?: "))
                    if amount >= bag[index]["Quantity"]:
                        bag.remove(bag[index])
                    else: bag[index]["Quantity"] -= amount
                    input("Item(s) removed\nHit ENTER: "); continue
                else: input("Invalid id\nHit ENTER: "); continue
                
            case 'b':
                for item in bag:
                    print(str(item["Quantity"])+"x\t"+item["Item"]["Item"]+f"\t£{int(item["Item"]['Price'])*item["Quantity"]}")
                input("Press ENTER: "); continue
            case 'p': 
                proceed = input("are you sure you want to check out? y/n: ").casefold()
                if proceed == 'n': continue

                receipt_gen.generate_receipt(bag)
                input("Press ENTER: "); running = False; continue
            case _: input("Unrecognized action: "); continue

class ToyStore:
    def __init__(self):
        # In-memory storage for stock and customers
        self.stock = []  # List to store items as dictionaries
        self.customers = []  # List to store customer information

    def add_stock_item(self, item_name, category, price):
        """Add a new item to the stock."""
        item = {
            "id": len(self.stock) + 1,  # Unique ID
            "name": item_name,
            "category": category,
            "price": price
        }
        self.stock.append(item)  # Add item to stock

    def get_all_stock(self):
        """Return all stock items."""
        return self.stock

    def search_stock(self, keyword):
        """Search stock by name or category."""
        results = []
        for item in self.stock:
            if keyword.lower() in item["name"].lower() or keyword.lower() in item["category"].lower():
                results.append(item)
        return results

    def save_customer(self, name, email, past_purchases):
        """Save a customer's details."""
        customer = {
            "id": len(self.customers) + 1,  # Unique ID
            "name": name,
            "email": email,
            "purchases": past_purchases
        }
        self.customers.append(customer)  # Add customer to the list

    def generate_receipt(self, purchased_items):
        """Generate a receipt for the purchased items."""
        total = 0
        receipt = "----- Receipt -----\n"
        for item in purchased_items:
            receipt += f"{item['name']} - ${item['price']}\n"
            total += item['price']

        # Apply discounts
        discount = 0
        toy_total = sum(item["price"] for item in purchased_items if item["category"] == "Toys")
        nursery_total = sum(item["price"] for item in purchased_items if item["category"] == "Nursery")

        if toy_total > 100:
            discount += toy_total * 0.10
        if nursery_total > 200:
            discount += nursery_total * 0.15

        receipt += f"Subtotal: ${total:.2f}\n"
        receipt += f"Discount: -${discount:.2f}\n"
        receipt += f"Total: ${total - discount:.2f}\n"
        receipt += "-------------------"
        return receipt

if __name__ == "__main__":
    # Program Workflow
    store = ToyStore()

    # Adding stock items
    store.add_stock_item("Brio Train Set", "Toys", 119)
    store.add_stock_item("Paw Patrol Tower", "Toys", 159)
    store.add_stock_item("Safari Animal Mobile", "Nursery", 30)
    store.add_stock_item("Chicco Crib", "Nursery", 199)

    # Display all stock
    print("All Stock:")
    for item in store.get_all_stock():
        print(f"ID: {item['id']}, Name: {item['name']}, Category: {item['category']}, Price: ${item['price']}")

    # Search for an item
    print("\nSearch Results for 'Toys':")
    for item in store.search_stock("Toys"):
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}")

    # Save a customer
    store.save_customer("Alice Smith", "alice@example.com", ["Brio Train Set", "Paw Patrol Tower"])

    # Generate a receipt
    purchased_items = [
        {"name": "Brio Train Set", "category": "Toys", "price": 119},
        {"name": "Safari Animal Mobile", "category": "Nursery", "price": 30},
        {"name": "Chicco Crib", "category": "Nursery", "price": 199}
    ]
    print("\nReceipt:")
    print(store.generate_receipt(purchased_items))
