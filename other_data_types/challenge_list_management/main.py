#1 inital list
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
#2 master list
deli_debt = [meat, cheese, condiment]
# 1st output req
print("Initial Deli List: ", deli_debt,".")
#
#3
if ("Ham" in meat) and (meat[2] <= 100):
    meat.pop(2) and meat.insert(2,100)      
#4 added list
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_debt.append(seasonal_meat)
#5 remove condiment
deli_debt.remove(condiment)
#6
deli_debt.sort()
#2nd output req
print("Updated Deli List:", deli_debt,".")
