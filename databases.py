import atexit
import csv
import os

class Database():
    def __init__(self, filepath:str, formatting:dict[dict] = None) -> None:
        # member variables of class // self note: DO NOT move out of __init__
        self.filepath = os.path.dirname(os.path.realpath(__file__))+'/'+filepath # sets the file path relative to the directory the program is in
        self.database:list[dict] = [] # a list of items in the database
        self.fields:list[str] = [] # fields for said list
        self.formatting = formatting

        # loads the database via the csv dict reader
        with open(self.filepath, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.database.append(line)
                self.database[-1]["Price"] = int(self.database[-1]["Price"])
        # sets the fields(keys) from the database
        if self.database:
            self.fields = self.database[0].keys()

        atexit.register(self.__on_destroy) # calls on exit of program // might want to use diff solution in future so changed data isn't lost on crash
                                         # DO NOT define any variable you will usee in this outside of __init__. It will apply to ALL instances of this class. I learnt this the hard way

    # called automatically when the program finishes execution // saves the database to the file incase it has changed // do not call manually
    def __on_destroy(self):
        if self.database!=[]:
            with open(self.filepath, "w") as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()
                writer.writerows(self.database)

    # handles conversion to str type when type cast with str()
    def __str__(self) -> str:
        text = ""
        for line in self.database:
            for key in self.fields:
                prefix = ''
                suffix = ''
                if self.formatting != None:
                    for fkey in self.formatting.keys():
                        if fkey == key:
                            prefix = self.formatting[fkey]["prefix"]
                            suffix = self.formatting[fkey]["suffix"]
                text += prefix+str(line[key])+suffix+", "
            text = text[:-2]+'\n'
        return text

    # used to search database // implementation (especially) not final so feedback is very welcome
    def search(self, field, value) -> list[dict]:
        results = []
        for item in self.database:
            if item[field] == value:
                results.append(item)
        return results

    # adds an item to the database // info should be in order of fields in csv file eg. for Item, Type, Price you would pass ["item name", "toy", 10]
    def add(self, info:list) -> None:
        item = {}
        for key,value in zip(self.fields, info):
            item[key] = value
        self.database.append(item)

    # removes items from database // implementation (especially) not final so feedback is very welcome
    def remove(self, field, value):
        found = False
        for item in self.database:
            if item[field] != None: 
                if item[field] == value: self.database.remove(item); found = True
        if not found: raise KeyError("item could not be found")

    # used to edit items // implementation (especially) not final so feedback is very welcome
    # USAGE: field to search eg. "Item", value eg. "example toy", fields you want to change eg. ["Type", "Price"], values to change to eg. ["Toys", 14]
    def edit(self, search_field, search_value, changed_fields:list, values:list):
        found = False
        for i, item in enumerate(self.database):
            if item[search_field] != None: 
                if item[search_field] == search_value:
                    for key, value in zip(changed_fields,values):
                        self.database[i][key] = value
                    found = True
        if not found: raise KeyError("item could not be found")

# stock and customer database init for later use in other parts of program
stock = Database("stock.csv", {"Price":{"prefix":"£", "suffix":""}})
customers = Database("customers.csv")


#only used for testing and won't run when included as library
if __name__ == "__main__":
    print(stock)
    print(stock.search("Item", "Brio train set"))
    #stock.add(["test thing", "Toy", 5])
    #stock.edit("Item", "test thing", ["Price", "Category"], [10, "Toys"])
    #stock.remove("Item", "test thing")
