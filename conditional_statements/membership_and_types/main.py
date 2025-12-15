# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
#store substring search
contains_raw = "raw" in description
contains_Imported = "Imported" in description
#store data types
price_is_float = type(price)
count_is_int = type(count)
#output
Print(Contains 'raw': <contains_raw>)
Print(Contains 'Imported': <contains_Imported>)
Print(Is price a float?: <price_is_float>)
Print(Is count an integer?: <count_is_int>)
