# Simple login system for customers and staff

# Customer login details (3 customers)
#User names are John, Jane and Alice with all passwords being "password"
customers = {
    'customer1': {'username': 'john', 'password': 'password'},
    'customer2': {'username': 'jane', 'password': 'password'},
    'customer3': {'username': 'alice', 'password': 'password'}
}

# Staff login details (shared for all staff)
staff = {'username': 'staff_user', 'password': 'staffpassword'}

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
