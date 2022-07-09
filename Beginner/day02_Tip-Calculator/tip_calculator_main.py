
# Input:
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
persons = input("How many people to split the bill? ")

# Caster alle variablene:
bill_float = float(total_bill)
tip_int = int(tip)
persons_int = int(persons)

# Regner prosent:
percent = tip_int / 100
amount_percent = bill_float * percent
totalBill_with_tip = bill_float + amount_percent

# Deler regning med tips på antall personer:
split_bill = totalBill_with_tip / persons_int
total = round(split_bill, 2)

# Output:
result = f"Each person should pay: ${total}"
print(result)
