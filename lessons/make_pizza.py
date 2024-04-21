"""Practice instantiating Pizza class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("large", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else: 
#         cost: 5.0
#     # charge 0.75 per topping
#     cost += 0.75 * pizza_order.toppings
#     # charge $1 for gf
#     if pizza_order.GF:
#         cost =+ 1.0
#     return cost

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())