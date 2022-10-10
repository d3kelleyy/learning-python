print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

party_count = int(input("How many people to split the bill? "))

party_bill = float((total_bill / party_count) * ((tip / 100) + 1))

print(f"Each person should pay: $" "{:.2f}".format(party_bill))