# Simple login system for customers and staff

import databases
import enum

class AccountErrorTypes(enum.Enum):
    UNRECOGNISED_ACCOUNT = 0

# Staff login details (shared for all staff)
staff_account = {'username': 'staff_user', 'password': 'staffpassword',"current_cart":["Chicco Crib"],"purchase_history":["Brio train set", "Paw Patrol tower", "Non existent item"]}

def login(username, password):    
    # Check if the username is valid and the password matches for the customer
    for customer in databases.customers.database:
        if customer['username'].lower() == username.lower() and customer['password'] == password:  # Convert stored username to lowercase
            return [customer, False]
    
    # does the same for staff
    if staff_account['username'].lower() == username.lower() and staff_account['password'] == password:
        return [staff_account, True]

    return [None, AccountErrorTypes.UNRECOGNISED_ACCOUNT]

if __name__ == "__main__":
    # Run the login function
    login()
