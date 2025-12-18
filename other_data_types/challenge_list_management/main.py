#1 inital list
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
#2 master list
deli_debt = [meat, cheese, condiment]
#3
if ("Ham" in meat) and (meat[2] <= 100):
else:
    ((meat.pop(2)) and (meat.insert(2,100))
      
#4 added list
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_debt.append(seasonal_meat)
#5 remove condiment
deli_debt.remove(condiment)
#6
deli_debt.sort