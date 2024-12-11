import accounts
import modes

def main():
    info = accounts.login()
    if info["staff"] == True:
        modes.staff()
    else: 
        modes.customer()

if __name__ == "__main__":
    main()