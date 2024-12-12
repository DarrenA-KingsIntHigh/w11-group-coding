import accounts
import modes
import os

def main():
    os.system('cls')
    print("Welcome to the system!\n")

    account_info = [None, None]
    while account_info[0] == None:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account_info = accounts.login(username,password)

        if account_info[0] == None:
            match account_info[1]:
                case accounts.AccountErrorTypes.UNRECOGNISED_ACCOUNT: 
                    input("Invalid username or password. Please try again: ")
        os.system('cls')
    
    input(f"Welcome, {account_info[0]['username']}! You have successfully logged.\nHit ENTER: ")
    if account_info[1] == True:
        modes.staff()
    else: 
        modes.customer()

if __name__ == "__main__":
    main()