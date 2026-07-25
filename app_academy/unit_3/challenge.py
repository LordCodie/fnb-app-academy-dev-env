user_distance = float(input("How many Kilometers do you want to drive?: "))

current_price_per_litre = float(input("What is the current price per litre?: "))

litres_needed = user_distance / 10

total_cost = litres_needed * current_price_per_litre

print(f"Final Cost: R {round(total_cost, 2)}")


