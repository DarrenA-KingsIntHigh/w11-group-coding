# a lot of this functionality is implemented in database.py. If you want to take a look in there I've left some comments for documentation
import databases # should import it unless there is another python module called databases I don't know about

def staff():
    pass

def customer():
    pass

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
