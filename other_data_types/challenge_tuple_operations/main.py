# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
#variables
apple_count = shelf.count("apples")
banana_index = shelf.index("bananas")
orange_index = shelf.index("oranges")
grape_count = shelf.count("grapes")
# apple logic
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
# grape logic
if grape_count >= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
#orange logic
if "oranges" in shelf:
    print("Oranges are at index:",orange_index)
else:
    print("Oranges are out of stock.")
#output
print("Number of Apples:", apple_count)
print("First Banana Index:",banana_index)
