vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")

if("carrots" not in vegetables):
    (vegetables.append("carrots"))
else:
    print("Carrots are already on the list.")

if ("cucumbers" not in vegetables):
    (vegetables.append("cucumbers"))
else: 
    print("Cucumbers are already on the list.")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)


