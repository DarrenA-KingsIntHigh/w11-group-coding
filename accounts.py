# Simple login system for customers and staff

import databases

# Staff login details (shared for all staff)
staff = {'username': 'staff_user', 'password': 'staffpassword',"current_cart":["Chicco Crib"],"purchase_history":["Brio train set", "Paw Patrol tower", "Non existent item"]}

def login():
    print("Welcome to the system!")
    
    while True:
        user_type = input("Are you a customer or staff? ").lower()

        if user_type == 'customer':
            while True:
                username = input("Enter your username: ").lower()  # Convert to lowercase
                password = input("Enter your password: ")

                # Check if the username is valid and the password matches for the customer
                for customer in databases.customers:
                    if customer['username'].lower() == username and customer['password'] == password:  # Convert stored username and password to lowercase
                        input(f"Welcome, {username}! You have successfully logged in as a customer.\nHit ENTER: ")
                        return [customer, False]

                input("Invalid username or password for customer. Please try again: ")
        
        elif user_type == 'staff':
            while True:
                username = input("Enter your username: ").lower()  # Convert to lowercase
                password = input("Enter your password: ")

                # Check if the username and password match for staff
                if staff['username'].lower() == username and staff['password'] == password:
                    print("Welcome, staff! You have successfully logged in.")
                    return [staff, True]
                else:
                    print("Invalid username or password for staff. Please try again.")
        
        else:
            print("Invalid user type. Please choose either 'customer' or 'staff'.")

if __name__ == "__main__":
    # Run the login function
    login()
