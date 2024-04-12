# Music Volumes
GENTLE_MUSIC_VOLUME = 2
MEDIUM_MUSIC_VOLUME = 6
LOUD_MUSIC_VOLUME = 11
MUSIC_VOLUME = GENTLE_MUSIC_VOLUME

WATER_PER_GUEST_IN_ML = 400
SPOONS_PER_GUEST = 2
WAIT_TIME_TO_TAKE_ORDER = 2

def serve_group_of_two():
    """
   Serves a party of two hungry customers.
   Ensures an unforgettable experience!
   """
    number_of_guests = 2
    greet_guests()
    table_number = prepare_table(number_of_guests)
    for guest in range(0, number_of_guests):
        lay_spoons_on_table(SPOONS_PER_GUEST)
    lead_customers_to_table(table_number)
    fill_water_carafe(number_of_guests * WATER_PER_GUEST_IN_ML)
    adjust_music_volume(MUSIC_VOLUME)
    present_menus(number_of_guests)
    wait_minutes(WAIT_TIME_TO_TAKE_ORDER)
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