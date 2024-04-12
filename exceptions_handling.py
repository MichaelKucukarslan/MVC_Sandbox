sequence = ["a", "b", "c", "d", "e"]

while True:
    try:
        index = int(input("Which index shall we look for? "))
        print("That was element", sequence[index])
    except IndexError:
        print("Not in range.")
    except ValueError:
        print("Not an integer.")