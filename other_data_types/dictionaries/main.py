#initial dictionary
grocery_inventory = {
    "Milk" : (113,"Dairy"),
    "Eggs":(116,"Dairy"),
    "Bread":(117,"Bakery"),
    "Apples":(141,"Produce")
}
#vars
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:",bread_details)

#logic
grocery_inventory["Cookies"] = (143,"Bakery")
print("Inventory after adding Cookies:",grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:",grocery_inventory)