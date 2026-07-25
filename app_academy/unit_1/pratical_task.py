print("Please enter your first name:")
first_name = input("")
print("Please enter your last name:")
last_name = input("")
print("Please enter your age:")
age = int(input(""))
print("Please enter your favourite number:")
favourite_number = float(input(""))

print(f"Welcome, {first_name.title() + " " + last_name.title()}")

print(f"Age in months: {age * 12}")

print(f"Favourite Number rounded to 2 decimal places: {round(favourite_number, 2)}")

print(f"Data type of each value:")
print(f"\t first name: {type(first_name)}")
print(f"\t last name: {type(last_name)}")
print(f"\t age: {type(age)}")
print(f"\t favourite number: {type(favourite_number)}")


