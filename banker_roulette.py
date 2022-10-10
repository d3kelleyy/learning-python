import random


names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")


index = random.randint(0, len(names) - 1)

choice = names[index]

print(f"{choice} is going to buy the meal.")
