# Inputs we need from the user
# Total rent
# Total food orderd for snacking
# Electicity units spend
# Charger per unit
# Persons living in room/float

## output
# Total amout you've  to pay is 

rent = int(input("Enter your hostel/flat rent =  "))
food = int(input("Enter the amount of food ordered =  "))
electricity_spend = int(input("Enter the  total of electricity spend =  "))
charger_per_unit = int(input("Enter the charger per unit = "))
persons = int(input("Enter the number of person living in room/flat = "))

total_bill = electricity_spend * charger_per_unit
