import json

food_descriptors = dict()
    
def write_db():
    open('C:\\Users\\jvansch1\\Documents\\Programming\\db.json', 'w').close()  #Delete contents of current file

    fh = open('C:\\Users\\jvansch1\\Documents\\Programming\\db.json', 'w')
    json.dump(food_descriptors, fh, indent=4)
    fh.close()

def load_db():
    fh = open('C:\\Users\\jvansch1\\Documents\\Programming\\db.json', 'r')
    global food_descriptors
    food_descriptors = json.load(fh)
    fh.close()

def lookup_aisle(food, coupon): 
    
    if food in food_descriptors and coupon == "yes":
        return (food.title() + " is in " + food_descriptors[food]['location'] + " and costs " + food_descriptors[food]['price'] + " and has a coupon.")
    elif food in food_descriptors and coupon == "no":
        return (food.title() + " is in " + food_descriptors[food]['location'] + " and costs " + food_descriptors[food]['price'])
    else:
        return ("This store doesn't carry " + food.title() + ".")

load_db()

while True:
    command = input("Enter Food Item (Enter ? for other command options): ")

    if command == "":
        pass2
    elif command == "?":
        print("Enter 'quit' to quit program")
        print("Enter 'save' to save program")
        print("Enter 'load' to load food database")
        print("Enter 'delete' to delete a food item")
        print("Enter 'add' to add a food item to the database")
    
    elif command == "quit":
        quit()
    elif command == "save":
        write_db()
    elif command == "load":
        load_db() 
    elif command == "delete":
        deleted_food_item = input("Enter the food item you would like to delete: ")
        del food_descriptors[deleted_food_item]
    elif command == "add":
        added_food_item = input("Enter a food item you would like to add: ")
        added_food_item_price = input("Enter the price: ")
        added_food_item_aisle = input("Enter the aisle it's located in: ")
        food_descriptors[added_food_item]={"price": added_food_item_price, "location": added_food_item_aisle}
    elif command == "debug":
        print(food_descriptors)
    else:
        coupon = input("Do you have a coupon (yes/no): ")
        print(lookup_aisle(command, coupon))
