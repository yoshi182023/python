"""Pizza order cost calculator."""

# Step 1: Get user input for pizza size, toppings, and delivery distance.
size = input("Choose your pizza size (small or large): ").lower()
topping_count = int(input("How many toppings would you like? "))
delivery_distance = int(input("How far is the delivery in miles? "))

# Step 2: Set the base price based on the selected pizza size.
if size == "small":
    pizza_cost = 8
elif size == "large":
    pizza_cost = 12
else:
    print("Invalid pizza size. Please enter 'small' or 'large'.")
    raise SystemExit

# Step 3: Calculate the topping cost.
topping_cost = topping_count * 1

# Step 4: Calculate the delivery fee based on distance.
if delivery_distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (delivery_distance - 5) * 1

# Step 5: Add all costs to get the total order cost.
total_cost = pizza_cost + topping_cost + delivery_fee

# Step 6: Display the final order details and total price.
print(f"Pizza size: {size}")
print(f"Number of toppings: {topping_count}")
print(f"Delivery distance: {delivery_distance} miles")
print(f"Total cost: ${total_cost:.2f}")
