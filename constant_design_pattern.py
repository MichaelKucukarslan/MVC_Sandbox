
def serve_group_of_two():
    """
   Serves a party of two hungry customers.
   Ensures an unforgettable experience!
   """
    greet_guests()
    table_number = prepare_table(2)
    for guest in range(0, 2):
        lay_spoons_on_table(2)
    lead_customers_to_table(table_number)
    fill_water_carafe(800)
    adjust_music_volume(2)
    present_menus(2)
    wait_minutes(2)
    drinks_order = take_order(table_number)
    process_order(drinks_order)
    # ...
    present_bill()
    thank_guests()

def prepare_table(number_of_guests):
    pass

def greet_guests():
    pass

def lay_spoons_on_table(number_of_spoons):
    pass

def lead_customers_to_table(table_number):
    pass

def fill_water_carafe(water_to_fill):
    pass

def adjust_music_volume(music_volume):
    pass

def present_menus(number_of_menus):
    pass

def wait_minutes(amount_to_wait):
    pass

def take_order(table_number):
    pass

def process_order(drinks_order):
    pass

def present_bill():
    pass

def thank_guests():
    pass