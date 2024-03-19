import random 
name = input("What is your first name? ")
print(name)
shoes = input("WHat shoes do you like? ")
rand = random.randint(1,5)
if rand == 1:
    print("I love those")
elif rand == 2:
    print("Nice choice")
elif rand == 3:
    print(shoes + "'s are my favorite")
elif rand == 4:
        print("I like your choice so far.")
elif rand == 5:
        print("My friend likes that as well.")
else:
    print("Nice, casual is always in!")

print()

age = input("How old are you? ")
print(age)
if age == 30:
    print("I think it's a little late to explore")
if age != 30:
    print("That's is a good age to start exploring style.")
print("I think I might know your style.")

print() 

top = input("So, " + name + ", what is your favorite top? ")
if top == "Graphic Tees":
    print("That's my favorite!")
elif top == "tank tops":
    print("That's a good choice.")
else: 
    print("We should have it!")
print("Ayy that's lit.")
print("I like where this is going.")

print()

bottom = input("What about your choice of bottom? ")
if bottom == "Cargos":
    print("I love " + bottom + " pants!")
elif bottom == "Shorts":
    print("Nice, we should have it.")
else:
    print("Nice, you never go wrong with those!")

print()

q1 = input("Anything else you want to add?")
if q1 == "yes":
    print("Well, " + name + ", it was awesome getting to know your style." )