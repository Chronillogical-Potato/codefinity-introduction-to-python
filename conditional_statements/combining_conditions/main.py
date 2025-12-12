# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = True if (discounted := True) or (lowStock := True) else False
promotion = True if (discounted := False) and (lowStock := False) else False

print(f"Is the item eligible for promotion? {promotion}.")