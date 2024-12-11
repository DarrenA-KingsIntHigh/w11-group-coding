# Simple login system for customers and staff

# Customer login details (3 customers)
# User names are John, Jane, and Alice with all passwords being "password"
customers = {
    'customer1': {'username': 'john', 'password': 'password'},
    'customer2': {'username': 'jane', 'password': 'password'},
    'customer3': {'username': 'alice', 'password': 'password'}
}

# Staff login details (shared for all staff)
staff = {'username': 'staff_user', 'password': 'staffpassword'}

# Sample product items (replacing menu)
products = {
    'Brio Train Set': 119.0,
    'Paw Patrol Tower': 159.0,
    'Safari Animal Mobile': 30.0,
    'Chicco Crib': 199.0
}

# Function to generate a receipt for the customer's order and save to a text file
def generate_receipt(order_items):
    total = sum(order_items[item]['total_price'] for item in order_items)
    receipt_content = "--- Receipt ---\n"
    
    for item, details in order_items.items():
        receipt_content += f"{item} (x{details['quantity']}): ${details['total_price']:.2f}\n"
    
    receipt_content += "----------------\n"
    receipt_content += f"Total: ${total:.2f}\n"
    receipt_content += "Thank you for your order!\n"

    # Save the receipt to a text file
    with open("receipt.txt", "w") as file:
        file.write(receipt_content)
    
    # Print the receipt to the console
    print("\n--- Receipt ---")
    print(receipt_content)

def place_order(username):
    print("\nWelcome to the Order System!")
    print("Products:")
    for item, price in products.items():
        print(f"{item}: ${price}")

    order_items = {}  # Dictionary to store customer's order

    while True:
        item = input("\nEnter the product you want to order (or type 'done' to finish): ").title()

        if item == 'Done':
            break

        if item in products:
            while True:
                try:
                    quantity = int(input(f"How many {item}s would you like to order? "))
                    if quantity < 1:
                        print("You must order at least 1 item. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            # If the item is already in the order, update the quantity and total price
            if item in order_items:
                order_items[item]['quantity'] += quantity
                order_items[item]['total_price'] = order_items[item]['quantity'] * products[item]
            else:
                # Add the new item to the order
                order_items[item] = {
                    'quantity': quantity,
                    'total_price': products[item] * quantity
                }
        else:
            print(f"Sorry, we don't have {item} in our product list. Please choose from the list.")

    # Generate and save the receipt
    generate_receipt(order_items)

def login():
    print("Welcome to the system!")
    
    while True:
        user_type = input("Are you a customer or staff? ").lower()

        if user_type == 'customer':
            while True:
                username = input("Enter your username: ").lower()  # Convert to lowercase
                password = input("Enter your password: ")

                # Check if the username is valid and the password matches for the customer
                for customer in customers.values():
                    if customer['username'].lower() == username and customer['password'] == password.lower():  # Convert stored username and password to lowercase
                        print(f"Welcome, {username}! You have successfully logged in as a customer.")
                        place_order(username)  # Allow the customer to place an order
                        return

                print("Invalid username or password for customer. Please try again.")
        
        elif user_type == 'staff':
            while True:
                username = input("Enter your username: ").lower()  # Convert to lowercase
                password = input("Enter your password: ").lower()  # Convert to lowercase

                # Check if the username and password match for staff
                if staff['username'].lower() == username and staff['password'].lower() == password:
                    print("Welcome, staff! You have successfully logged in.")
                    return
                else:
                    print("Invalid username or password for staff. Please try again.")
        
        else:
            print("Invalid user type. Please choose either 'customer' or 'staff'.")

# Run the login function
login()
