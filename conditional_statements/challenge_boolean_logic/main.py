#pre-defined
seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
#is the item seasonal and overstocked?
overstock_risk = seasonal and current_stock >= high_stock_threshold
#discount when NOT on_sale and NOT selling_well
discount_eligible = not selling_well and not on_sale
#need to discount when overstocked or eligible
make_discount = overstock_risk or discount_eligible
#ye or ne?
print(f"Should the item be discounted? {make_discount}.")