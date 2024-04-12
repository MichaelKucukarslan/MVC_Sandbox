def hawaiian():
    # Preparation tasks for any pizza
    roll_dough()
    spread_tomato_sauce()
    sprinkle_cheese()
    # Tasks unique to this pizza
    chop_pineapple()
    dice_ham()
    # Final tasks for any pizza
    bake_in_pizza_oven()
    serve_on_plate()

def vegetarian():
    # Preparation tasks for any pizza
    roll_dough()
    spread_tomato_sauce()
    sprinkle_cheese()
    # Tasks unique to this pizza
    slice_peppers()
    dice_onion()
    chop_tomatoes()
    # Final tasks for any pizza
    bake_in_pizza_oven()
    serve_on_plate()

def pepperoni():
    print("Adding pepperoni")


def make_most_pizzas(special_instructions):
    def wrapper():
        roll_dough()
        spread_tomato_sauce()
        sprinkle_cheese()
        special_instructions()
        bake_in_pizza_oven()
        serve_on_plate()
    return wrapper

pepperoni_pizza = make_most_pizzas(pepperoni)
# pepperoni_pizza()

def roll_dough():
    print("Rolling Dough")

def spread_tomato_sauce():
    print("Rolling Dough")

def sprinkle_cheese():
    print("sprinkling cheese")

def bake_in_pizza_oven():
    print("Baking Pizza")

def serve_on_plate():
    print("Serving Pizza")

def chop_pineapple():
    print("Chopping pineapple")

def dice_ham():
    print("Dicing ham")

def slice_peppers():
    print("slicing peppers")

def dice_onion():
    print("Dicing Onions")

def chop_tomatoes():
    print("Chopping tomatoes")

if __name__ == "__main__":
    pepperoni_pizza()