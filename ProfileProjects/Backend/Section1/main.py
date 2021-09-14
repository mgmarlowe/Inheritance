import sys
# Import pickle to save game
import pickle
# Import os.path to check if save file exists
import os.path
save_exists = os.path.isfile("data.pickle")


# === Menu options and utility functions


def menu(choice):
    if choice[0].lower() == "m":
        print_menu()
    elif choice[0].lower() == "s":
        save()
    elif choice[0].lower() == "d":
        delete()
    elif choice[0].lower() == "h":
        help()
    elif choice[0].lower() == "i":
        inventory()
    elif choice[0].lower() == "e":
        save()
        print("See you next time!")
        sys.exit()


def print_menu():
    print("\nAccess options with the following choices:")
    print("   m : Display the menu of options")
    print("   s : Save the game")
    print("   d : Delete your current save file")
    print("   h : Display help screen")
    print("   i : Display inventory")
    print("   e : Save and exit game")
    return


def inventory():
    # TODO show inventory
    print("\nInventory:")
    inventory = (data["inventory"].values())
    for item in inventory:
        print(" - ", item)

def update_inv(items):
    data["inventory"].update(items)
    inventory()
    return


def help():
    print("\nEnter the number of your choice to move around the house and grounds\nor enter a menu option to see other choices.")
    print_menu()
    return


def get_choice(options):
    menu_options = ("m", "s", "d", "h", "i", "e")
    while True:
        choice = input("\nMake a choice: ")
        if choice in options:
            return choice
        elif choice[0] in menu_options:
            menu(choice)
        else:
            print("Invalid choice")



# --- Start of game function, only runs once per game

def start():
    print("\n\nWelcome to Inheritance, a room escape style text adventure! \nTo make choices, enter the number associated with your choice and hit enter. \nIf you need help or would like to know more about other choices you can make, type in 'help' or just an 'h' at any time. \nThank you for playing, and enjoy the journey!\n\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("================================")
    print("-----------Inheritance----------")
    print("================================")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\n\n")
    print("Your uncle has been missing since you were a child. Though the reasons were never discovered, and no missing person report had been made. Your family never knew what had happened, but he had left controll of his house and estate to his lawyer. Per his instructions, the lawyer was not at liberty to discuss the instructions left, and the mystery remained just that.\n\n Now, however, his lawyer has contacted you to say that the allotted time has passed, and you have been bequeathed his house and property. They can't come with you to the house, but told you they left a key 'Under the unwelcome mat,' whatever that means. \n\nYou're standing on the sidewalk in front of the house, which has been maintained by his lawyers over the years. The door is a calm light grey. \nTo the left, you see a path to the back of the house. \nTo the right, you see a smaller building, possibly a shed.\n")
    print("1) Go to the house")
    print("2) Go to the path")
    print("3) Go to the shed")
    print("4) Leave. You can just sell the house. Who cares what happened, anyway?")
    options = ("1", "2", "3", "4")
    choice = get_choice(options)
    if choice == "1":
        front_door()
    elif choice == "2":
        path_split()
    elif choice == "3":
        shed_door()
    elif choice == "4":
        print("You walk away. You'll sell the house for a pretty penny. Oh well.")
        sys.exit()


# ======   Areas associated with House   ======


def front_door():
    print("\nThe door is a light grey, with bits of paint flecking off. There's dark blue paint beneath. There's a mat in front of the door that says 'Welcome.' There is a  metal mailbox under the doorbell.")
    print("\n1) Go through the door")
    print("2) Check the mailbox")
    print("3) Check under the mat")
    print("4) Go to the front yard")
    options = ("1", "2", "3", "4")
    choice = get_choice(options)
    if choice == "1":
        global data
        if "grey_door_key" in data["inventory"]:
            print("\nYou try each key on the ring. The one with the grey cover fits the lock, and you unlock the door.\n")
            data["front_door"] = True
            del data["inventory"]["grey_door_key"]
            foyer()
        elif data["front_door"] == True:
            foyer()
        else:
            print("\nYou try the door, but it's locked. Maybe there's a key somewhere...")
            front_door()
    if choice == "2":
        if data["mailbox"] == True:
            print("\nYou open the mailbox. There's nothing inside.")
            front_door()
        elif "mailbox_key" in data["inventory"]:
            data["mailbox"] = True
            del data["inventory"]["mailbox_key"]
            print("\nYou open the mailbox. Inside is a keyring with three keys. One has a grey cover, one has a red cover, and one has a blue cover.")
            items = {"grey_door_key" : "A door key with a grey cover", 
            "red_door_key" : "A door key with a red cover",
            "blue_door_key" : "A door key with a blue cover"}
            update_inv(items)
            front_door()
        else:
            print("The mailbox is locked.")
            front_door()
    if choice == "3":
        print("There's nothing under here...")
        front_door()
    if choice == "4":
        front_yard()


def front_yard():
    print("\nYou stand in the front yard. In front of you is the house, the door a calm light grey. To the left, you see a path to the back of the house. To the right, you see a shed.")
    print("\n1) Go to the house")
    print("2) Go to the path")
    print("3) Go to the shed")
    options = ("1", "2", "3")
    choice = get_choice(options)
    if choice == "1":
        front_door()
    elif choice == "2":
        path_split()
    elif choice == "3":
        shed_door()

def foyer():
    print("You're in a foyer. There is an open doorway to the left that you glimpse a table through. It must be the dining room. To the right is another open doorway, leading to what you know is the living room. The open doorway in front of you leads to the hallway. There is a closed closet door beside the hall doorway.")
    print("1) Go to the dining room")
    print("2) Go to the living room")
    print("3) Go to the hallway")
    print("4) Open the closet")
    print("5) Go out the front door")
    options = ("1", "2", "3", "4", "5",)
    choice = get_choice(options)
    if choice == "1":
        dining_room()
    elif choice == "2":
        living_room()
    elif choice == "3":
        hallway()
    elif choice == "4":
        closet()
    elif choice == "5":
        front_door()


def dining_room():
    global data

    print("The dining room has a table with six chairs, and a china hutch one wall. A swinging door is on the far side of the room. Art hangs on the wall. You recognize your uncle's style, though not the subjects.")

    if "dining_room_painting" not in data["inventory"]:
        print("Most are nature scenes you don't recognize, but one is of a woman.. She is lovely in a way that makes your eyes hurt.")
    else:
        print("The frame that once held the painting still has shreds of tattered canvas at the edges. It makes you feel uneasy...")

    print("1) Go to the foyer")
    print("2) Go through the swinging door")
    
    if "dagger" in data["inventory"] and "dining_room_painting" not in data["inventory"]:
        print("3) Cut down the painting")
        options = ("1", "2", "3")
        choice = get_choice(options)
    else:
        options = ("1", "2")
        choice = get_choice(options)

    if choice == "1":
        foyer()
    elif choice == "2":
        kitchen()
    elif choice == "3":
        print("You use the dagger to slice down the painting. There is a horrible pressure against your mind and your ears, like someone is screaming, and then it's done. You have the horrible, lovely painting. You fold it roughly to keep from seeing it.")
        items = {"dining_room_painting" : "Roughly folded canvas, a painting of the terrible woman."}
        update_inv(items)
        dining_room()


def kitchen():
    print("The kitchen has been unused for some time. The chrome appliances have been turned back off by the lawyer's office years ago. The cabinets are dark wood and the floor is tile laminate. The fridge has papers on it, but you can't tell what they are. A closed door, the hallway, is on the wall opposite the sink. You wonder if the cabinets hold any snacks...")
    print("1) Check the cabinets")
    print("2) Check the fridge")
    print("3) Go to the hallway")
    print("4) Go to the dining room")

    options = ("1", "2", "3", "4")
    choice = get_choice(options)

    if choice == "1":
        print("The cabinets hold the usual assortment of dishes and tools. There's a few cans of food, old labels and dusty. Inside one cabinet is a scrawled note, the marker almost invisible againt the dark wood. \n\n'Don't trust it...'")
        kitchen()
    elif choice == "2":
        fridge()
    elif choice == "3":
        hallway()
    elif choice == "4":
        dining_room()


def fridge():  # TODO rewrite to take out photo from description if it's in inventory
    print("The fridge has the usual types of papers on it. There are several old takeout menus, a child's drawing that you recognize as your own work, and a dry-erase board with a photo stuck in the corner.")
    print("1) Look at your drawing")
    print("2) Take the photo")
    print("3) Look in the fridge")
    print("4) Go back to looking through the kitchen")

    options = ("1", "2", "3", "4",)
    choice = get_choice(options)

    if choice == "1":
        print("You don't remember drawing this one, but it's definitely yours. It has you and your uncle and a treehouse. Where were you drawing?")
        fridge()
    elif choice == "2":
        print('It\'s a photo of a woman.. She\'s looking at something off camera. You find yourself oddly relieved she\'s not looking at you... There\'s a note written on it. \n\n"Such glamour I have never seen..."')
        items = {"fridge_photo" : "A photo of a terribly lovely woman..."}
        update_inv(items)
        fridge()


def living_room():
    print("Living room is still under construction")


def hallway():
    print("Hallway is still under construction")


def closet():
    print("Closet is still under construction")



def mudroom():
    print("Mudroom still under construction")
    return



# ======   Areas associated with Shed   ======


def shed_door():
    print("Shed Door still under construction")
    return

def treehouse():
    print("Treehouse still under construction")
    return


# ======   Areas associated with Back Yard   ======


def path_split():
    print("\nYou see a gazebo on the left and a patio to the right.\n")
    print("1) Go to the gazebo")
    print("2) Go to the patio")
    print("3) Go to the front yard")
    options = ("1", "2", "3")
    choice = get_choice(options)
    if choice == "1":
        gazebo()
    elif choice == "2":
        patio()
    elif choice== "3":
        front_yard()


def gazebo():
    print("\nYou enter the gazebo. It's nice, if run down. There are flower boxes along the outside, but they've been empty for years.\n")
    print("1) Go back to the path")
    print("2) Check the flower boxes")
    options = ("1", "2")
    choice = get_choice(options)
    if choice == "1":
        path_split()
    elif choice == "2":
        print("\nThe boxes certainly are empty.\n")
        gazebo()


def patio():
    global data
    print("\nThe patio is stone, though there are weeds pushing through the cracks. There's an old fountain to one side, maybe it was once lovely, but now it's covered in grime and moss. The opposite side of the patio has a covered fire pit, the stones have held up fairly well, but a few have fallen down. In the middle of the patio is a rusty set of chairs and a small cafe table, overlooking the overgrown back yard. There is a door into the house on the patio as well. ")
    if data["treehouse"] == True:
        print("\nNow that you know what to look for, you can see the hint of the path to the treehouse out behind the shed.")
    print("\n1) Check the fountain")
    print("2) Check the table")
    print("3) Check the fire pit")
    print("4) Check the door")
    print("5) Go to the path")

    if data["treehouse"] == True:
        print("6) Go to the treehouse")
        options = ("1", "2", "3", "4", "5", "6")
        choice = get_choice(options)
    else:
        options = ("1", "2", "3", "4", "5",)
        choice = get_choice(options)

    if choice == "1":
        fountain()
    elif choice == "2":
        table()
    elif choice == "3":
        fire_pit()
    elif choice == "4":
        back_door()
    elif choice == "5":
        path_split()
    elif choice == "6" and data["treehouse"] == True:
        treehouse()


def fountain():
    global data
    print("\nCloser up, the fountain isn't quite as grimy as you thought, but it's still got muck built up at the bottom. Most of the discoloration is just some nice, soft moss covering the stone. ")
    
    if "pail" not in data["inventory"]:
        print("An old pail is on its side at the bottom.")
        print("\n1) Go back to the patio")
        print("2) Pick up the pail")
        options = ("1", "2")
        choice = get_choice(options)
    else:
        print("1) Go back to the patio")
        options = ("1")
        choice = get_choice(options)

    if choice == "1":
        patio()
    elif choice == "2":
        print("You now have the pail. It's still pretty gross....")
        items = {"pail" : "An old pail. It's pretty gross..."}
        update_inv(items)
        fountain()


def table():
    global data
    print("The table is pretty rusty, and so are the chairs. Some of the bars look loose..")
    print("1) Check the bars")
    print("2) Go back to the patio")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        if "rusty_bar" in data["inventory"]:
            print("There are no more loose bars.")
            table()
        else:
            print("You wiggle some of the bars and one breaks off in your hand. You now have a rusty bar. You try to remember when you had your last tetanus shot...")
            items = {"rusty_bar": "A rusty iron bar. When did you have your last tetanus shot..."}
            update_inv(items)
            table()
    elif choice == "2":
        patio()


def fire_pit():
    print("Fire pit")
    #TODO Write fire pit function


def back_door():
    print('The door is faded blue, and there is an old mat that says "Oh, it\'s you..."')
    print("1) Go through the door")
    print("2) Check under the mat")
    print("3) Go back to patio")
    
    options = ("1", "2", "3")
    choice = get_choice(options)
    global data

    if choice == "1":
        if "blue_door_key" in data["inventory"]:
            mudroom()
        else:
            print("The door is locked...")
            back_door()
    elif choice == "2":
        if "blue_door_key" in data["inventory"]:
            print("There's nothing else under here.")
        else:
            print("You now have a small metal key! It's too small for a door...")
            items = {"mailbox_key" : "A small metal key."}
            update_inv(items)
            back_door()
    elif choice == "3":
        patio()



#   ======   Game save functions   ======


# use pickle to save game data
def save():
    pickle_out = open("data.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    print("Game saved")
    return

# use pickle to load game data
def load():
    if save_exists:
        pickle_in = open("data.pickle", "rb")
        global data
        data = pickle.load(pickle_in)
    else:
        print("No save file")
    global room
    room = data["room"]()

def delete():
    if save_exists:
        choice = input("Are you sure you want to delete your save file? Doing so will end this game. ").lower()
        if choice[0].strip() == "y":
            os.remove("data.pickle")
            sys.exit()
        else:
            print("Save file retained")
            return
    else:
        print("No save exists")
        return


# ======   Save and check data   ======


data = {
    "room" : start,
    "treehouse" : False,
    "front_door" : False,
    "mailbox" : False,
    "inventory" : {}
}

load()