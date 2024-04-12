def make_most_pizzas(special_instructions):
    def wrapper():
        roll_dough()
        spread_tomato_sauce()
        sprinkle_cheese()
        special_instructions()
        bake_in_pizza_oven()
        serve_on_plate()
    return wrapper

@make_most_pizzas
def hawaiian(): 
    # Tasks unique to this pizza
    chop_pineapple()
    dice_ham()

@make_most_pizzas
def vegetarian():
    # Tasks unique to this pizza
    slice_peppers()
    dice_onion()
    chop_tomatoes()
    
@make_most_pizzas
def pepperoni():
    print("Adding pepperoni")


# pepperoni_pizza = make_most_pizzas(pepperoni)
# pepperoni_pizza()

def roll_dough():
    print("Rolling Dough")

def spread_tomato_sauce():
    print("Spreading sauce")

def sprinkle_cheese():
    print("Sprinkling Cheese")

def bake_in_pizza_oven():
    print("Baking Pizza")

def serve_on_plate():
    print("Serving Pizza")

def chop_pineapple():
    print("Chopping pineapple")

def dice_ham():
    print("Dicing ham")

def slice_peppers():
    print("Slicing Peppers")

def dice_onion():
    print("Dicing Onions")

def chop_tomatoes():
    print("Chopping Tomatoes")

def print_space():
    print("----------")

if __name__ == "__main__":
    print_space()
    pepperoni()
    print_space()
    hawaiian()
    print_space()
    vegetarian()
    print_space()
