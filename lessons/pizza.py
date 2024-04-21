"""Define Pizza class."""

class Pizza:

    # attributes
    size: str # small or large
    toppings: int
    GF: bool

    def __init__(self, size_input: str, toppings_input: int, GF_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.GF = GF_input
        # it actually returns self

    def price(self) -> float:
        """calculate and return cost of pizza."""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else: 
            cost: 5.0
        # charge 0.75 per topping
        cost += 0.75 * self.toppings
        # charge $1 for gf
        if self.GF:
            cost =+ 1.0
        return cost
    
    def add_toppings(self, num_toppings: int) -> None:
        """Add number of toppings."""
        self.toppings += num_toppings