# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
#store substring search
contains_raw = "raw" in description
contains_Imported = "Imported" in description
#store data types
price_is_float = (type(price) == float)
count_is_int = (type(count) == int)
#output
print(Contains 'raw': <contains_raw>)
print(Contains 'Imported': <contains_Imported>)
print(Is price a float?: <price_is_float>)
print(Is count an integer?: <count_is_int>)
