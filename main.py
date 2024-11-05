import pprint
import os
cat_attributes = {
    "intelligence": 20,
    "energy": 50,
    "weight": 30,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
# ...

# start the while loop
while cat_attributes["energy"]>0 and cat_attributes["intelligence"]>0 and cat_attributes["weight"]>0:
    os.system('clear')
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3.  Feed it 4. Let it sleep 5. Show stats  \n")
    pprint.pprint(cat_attributes)
    if option == '1':
        cat_attributes["energy"] += 10
        cat_attributes["weight"] += -5
        pass
    elif option == '2':
        cat_attributes["intelligence"] += 10
        pass
    # elif ...
    elif option == '3':
        cat_attributes["weight"] += 10
        cat_attributes["energy"] += -5
    elif option == '4':
        cat_attributes["energy"] += 25
        cat_attributes["intelligence"] += -10





print(name, " is dead")


    