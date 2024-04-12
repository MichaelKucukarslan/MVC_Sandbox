sequence = ["a", "b", "c", "d", "e"]
 
while True:
    try:
        index = int(input("Which index shall we look for? "))
        print("That was element", sequence[index])