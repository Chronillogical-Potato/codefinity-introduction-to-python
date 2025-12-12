# The item's discount and stock status have been defined
discounted = False
lowStock = True
#Check if either is true
movingProduct = discounted or lowStock
#Check if not discounted and not lowStock
promotion = not discounted and not lowStock

print(f"Is the item eligible for promotion? {promotion}.")