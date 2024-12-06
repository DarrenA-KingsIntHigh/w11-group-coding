import atexit
import csv
import os

class Database():
    def __init__(self, filepath:str):
        self.filepath = os.path.dirname(os.path.realpath(__file__))+'/'+filepath
        self.database:list[dict] = []
        self.fields:list[str] = []

        with open(self.filepath, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.database.append(line)
                self.database[-1]["Price"] = int(self.database[-1]["Price"])

        if self.database:
            self.fields = self.database[0].keys()

        atexit.register(self.on_destroy) # calls on exit of program // might want to use diff solution in future so changed data isn't lost on crash
                                         # DO NOT define any variable you will usee in this outside of __init__. It will apply to ALL instances of this class. I learnt this the hard way

    def on_destroy(self):
        if self.database!=[]:
            with open(self.filepath, "w") as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()
                writer.writerows(self.database)

    def __str__(self):
        text = ""
        for line in self.database:
            for key in self.fields:
                text += str(line[key])+", "
            text = text[:-2]+'\n'
        return text

    def search(self, field, value):
        results = []
        for item in self.database:
            if item[field] == value:
                results.append(item)
        return results

    def add(self, info:list):
        item = {}
        for key,value in zip(self.fields, info):
            item[key] = value
        self.database.append(item)

    def remove(self, field, value):
        found = False
        for item in self.database:
            if item[field] != None: 
                if item[field] == value: self.database.remove(item); found = True
        if not found: raise KeyError("item could not be found")

    def edit(self, search_field, search_value, changed_fields:list, values:list):
        found = False
        for i, item in enumerate(self.database):
            if item[search_field] != None: 
                if item[search_field] == search_value:
                    for key, value in zip(changed_fields,values):
                        self.database[i][key] = value
                    found = True
        if not found: raise KeyError("item could not be found")

stock = Database("stock.csv")
customers = Database("customers.csv")


if __name__ == "__main__":
    print(stock)
    print(stock.search("Item", "Brio train set"))
    #stock.add(["test thing", "Toy", 5])
    #stock.edit("Item", "test thing", ["Price", "Category"], [10, "Toys"])
    #stock.remove("Item", "test thing")
