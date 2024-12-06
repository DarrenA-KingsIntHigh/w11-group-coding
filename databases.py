import csv
import os

class Database():
    database:list = []
    feilds:list = []
    def __init__(self, filepath:str, feilds:list):
        with open(os.path.dirname(os.path.realpath(__file__))+'/'+filepath, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.database.append(line)

        self.feilds = feilds

    def __del__(self):
        pass

    def __str__(self):
        text = ""
        for line in self.database:
            text += line["Item"]+" | "+line["Category"]+" | £"+line["Price"]+"\n"
        return text

    def search(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def edit(self):
        pass

stock = Database("stock.csv",[])
customers = Database("customers.csv",[])


if __name__ == "__main__":
    print(stock)
