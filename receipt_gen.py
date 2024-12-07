# Simple login system for customers and staff

# Darren - just a heads up I saw you copied a lot of code from your accounts.py program
# so I just wanted to let you know in case you didn't that you can do
# import accounts
# to include the code from that in here kind of like header files in C or C++
# but since all the program needs to generate a receipt and calculate the discount is the items ordered it probably doesn't need access to accounts

# EDIT: I just saw your commit message. I was thinking we'd use a more modular approach where each file contains a separate "module/idependant part/whatever" \n
# of the program and we just use import to include them in the parts that need them but I'm also totally down for going this approach I'd just want to discuss it first to make sure everyone's on the same page

# Customer login details (3 customers)
# User names are John, Jane, and Alice with all passwords being "password"
customers = {
    'customer1': {'username': 'john', 'password': 'password'},
    'customer2': {'username': 'jane', 'password': 'password'},
    'customer3': {'username': 'alice', 'password': 'password'}
}

# Staff login details (shared for all staff)
staff = {'username': 'staff_user', 'password': 'staffpassword'}

# Sample menu items
menu = {
    'Brio Train Set': 119.0,
    'Paw Patrol Tower': 159.0,
    'Safari Animal Mobile': 30.0,
    'Chicco Crib': 199.0
}

# Function to generate a receipt for the customer's order and save to a text file
def generate_receipt(order_items):
    total = sum(order_items.values())
    receipt_content = "--- Receipt ---\n"
    
    for item, price in order_items.items():
        receipt_content += f"{item}: ${price}\n"
    
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
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    order_items = {}  # Dictionary to store customer's order

    while True:
        item = input("\nEnter the item you want to order (or type 'done' to finish): ").title()

        if item == 'Done':
            break

        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            order_items[item] = menu[item] * quantity
        else:
            print(f"Sorry, we don't have {item} on the menu. Please choose from the list.")

    # Generate and save the receipt
    generate_receipt(order_items)

def login():
    print("Welcome to the system!")
    user_type = input("Are you a customer or staff? ").lower()

    if user_type == 'customer':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        # Check if the username is valid and the password matches for the customer
        for customer in customers.values():
            if customer['username'] == username and customer['password'] == password:
                print(f"Welcome, {username}! You have successfully logged in as a customer.")
                place_order(username)  # Allow the customer to place an order
                return
        
        print("Invalid username or password for customer. Please try again.")
        
    elif user_type == 'staff':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password match for staff
        if username == staff['username'] and password == staff['password']:
            print("Welcome, staff! You have successfully logged in.")
            return
        else:
            print("Invalid username or password for staff. Please try again.")
    else:
        print("Invalid user type. Please choose either 'customer' or 'staff'.")

# Run the login function
login()
