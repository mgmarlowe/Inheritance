# Import textwrap.fill to structure text
from textwrap import fill
# Import sys to exit
import sys
# Import pickle to save game
import pickle
# Import os.path to check if save file exists
import os.path
save_exists = os.path.isfile("data.pickle")
# Import time to delay events with time.sleep()
import time


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
    print("\nInventory:")
    inventory = (data["inventory"].values())
    for item in inventory:
        print(" - ", item)

def update_inv(items):
    data["inventory"].update(items)
    inventory()
    return


def help():
    print(fill("\nEnter the number of your choice to move around the house and grounds\nor enter a menu option to see other choices."))
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
    print(fill("\n\nWelcome to Inheritance, a room escape style text adventure! \nTo make choices, enter the number associated with your choice and hit enter. \nIf you need help or would like to know more about other choices you can make, type in 'help' or just an 'h' at any time. \nThank you for playing, and enjoy the journey!\n\n"))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("================================")
    print("-----------Inheritance----------")
    print("================================")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n\n\n")
    print(fill("Your uncle has been missing since you were a child. Though the reasons were never discovered, and no missing person report had been made. Your family never knew what had happened, but he had left controll of his house and estate to his lawyer. Per his instructions, the lawyer was not at liberty to discuss the instructions left, and the mystery remained just that.\n\n Now, however, his lawyer has contacted you to say that the allotted time has passed, and you have been bequeathed his house and property. They can't come with you to the house, but told you they left a key 'Under the unwelcome mat,' whatever that means. \n\nYou're standing on the sidewalk in front of the house, which has been maintained by his lawyers over the years. The door is a calm light grey. \nTo the left, you see a path to the back of the house. \nTo the right, you see a smaller building, possibly a shed.\n\n"))
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
    print(fill("\nThe door is a light grey, with bits of paint flecking off. There's dark blue paint beneath. There's a mat in front of the door that says 'Welcome.' There is a  metal mailbox under the doorbell."))
    print("\n1) Go through the door")
    print("2) Check the mailbox")
    print("3) Check under the mat")
    print("4) Go to the front yard")
    options = ("1", "2", "3", "4")
    choice = get_choice(options)
    if choice == "1":
        global data
        if "grey_door_key" in data["inventory"]:
            print(fill("\nYou try each key on the ring. The one with the grey cover fits the lock, and you unlock the door.\n"))
            data["front_door"] = True
            del data["inventory"]["grey_door_key"]
            foyer()
        elif data["front_door"] == True:
            foyer()
        else:
            print(fill("\nYou try the door, but it's locked. Maybe there's a key somewhere..."))
            front_door()
    if choice == "2":
        if data["mailbox"] == True:
            print("\nYou open the mailbox. There's nothing inside.")
            front_door()
        elif "mailbox_key" in data["inventory"]:
            data["mailbox"] = True
            del data["inventory"]["mailbox_key"]
            print(fill("\nYou open the mailbox. Inside is a keyring with three keys. One has a grey cover, one has a red cover, and one has a blue cover."))
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
    print(fill("\nYou stand in the front yard. In front of you is the house, the door a calm light grey. To the left, you see a path to the back of the house. To the right, you see a shed."))
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
    print(fill("\nYou're in a foyer. There is an open doorway to the left that you glimpse a table through. It must be the dining room. To the right is another open doorway, leading to what you know is the living room. The open doorway in front of you leads to the hallway. There is a closed closet door beside the hall doorway."))
    print("\n1) Go to the dining room")
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

    print(fill("\nThe dining room has a table with six chairs, and a china hutch one wall. A swinging door is on the far side of the room. Art hangs on the wall. You recognize your uncle's style, though not the subjects."))

    if "dining_room_painting" not in data["inventory"]:
        print(fill("Most are nature scenes you don't recognize, but one is of a woman.. She is lovely in a way that makes your eyes hurt."))
    else:
        print(fill("The frame that once held the painting still has shreds of tattered canvas at the edges. It makes you feel uneasy..."))

    print("\n1) Go to the foyer")
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
        print(fill("\nYou use the dagger to slice down the painting. There is a horrible pressure against your mind and your ears, like someone is screaming, and then it's done. You have the horrible, lovely painting. You fold it roughly to keep from seeing it."))
        items = {"dining_room_painting" : "Roughly folded canvas, a painting of the terrible woman."}
        update_inv(items)
        data["works"] += 1
        dining_room()


def kitchen():
    print(fill("\nThe kitchen has been unused for some time. The chrome appliances have been turned back off by the lawyer's office years ago. The cabinets are dark wood and the floor is tile laminate. The fridge has papers on it, but you can't tell what they are. A closed door, the hallway, is on the wall opposite the sink. You wonder if the cabinets hold any snacks..."))
    print("\n1) Check the cabinets")
    print("2) Check the fridge")
    print("3) Go to the hallway")
    print("4) Go to the dining room")

    options = ("1", "2", "3", "4")
    choice = get_choice(options)

    if choice == "1":
        print(fill("\nThe cabinets hold the usual assortment of dishes and tools. There's a few cans of food, old labels and dusty. Inside one cabinet is a scrawled note, the marker almost invisible againt the dark wood. \n\n'Don't trust it...'"))
        kitchen()
    elif choice == "2":
        fridge()
    elif choice == "3":
        hallway()
    elif choice == "4":
        dining_room()


def fridge():  # TODO rewrite to take out photo from description if it's in inventory
    print(fill("\nThe fridge has the usual types of papers on it. There are several old takeout menus, a child's drawing that you recognize as your own work, and a dry-erase board with a photo stuck in the corner."))
    print("\n1) Look at your drawing")
    print("2) Take the photo")
    print("3) Look in the fridge")
    print("4) Go back to looking through the kitchen")

    options = ("1", "2", "3", "4",)
    choice = get_choice(options)

    if choice == "1":
        print(fill("You don't remember drawing this one, but it's definitely yours. It has you and your uncle and a treehouse. Where were you drawing?"))
        fridge()
    elif choice == "2":
        print(fill('It\'s a photo of a woman.. She\'s looking at something off camera. You find yourself oddly relieved she\'s not looking at you... There\'s a note written on it. \n\n"Such glamour I have never seen..."'))
        items = {"fridge_photo" : "A photo of a terribly lovely woman..."}
        update_inv(items)
        data["works"] += 1
        fridge()
    elif choice == "3":
        print("How long has this mustard been waiting here...")
        fridge()
    elif choice == "4":
        kitchen()


def living_room():
    print(fill("\nThe living room furniture has been covered in dust cloths. Under those, you see rich red fabric, undisturbed by time. There are shelves on the wall,  mostly filled with knick-knacks and trinkets. Charcoal sketches hang on the wall. "))
    print("\n1) Check the knick-knacks and trinkets")
    print("2) Go back to the foyer")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        print(fill("\nThe decorative odds and ends don't clutter the room, and the shelves seem to have different themes. The actual shelves double as art, in interesting geometric patterns. One shelf hold a variety of crystals and stones. Another holds dried flowers. One interesting little cabinet with a door has different bottles in weird shapes, with colorful liquids inside."))
        foyer()
    elif choice == "2":
        foyer()


def hallway():
    print(fill("\nThe hallway seems to stretch the whole house. There is an open door to a bathroom. On the same side is an open door leading to a study, and a hallway. The opposite side of the hall has a door to the kitchen and a closed door with a star painted on it. On one far side is a mud room with the doorway to the back patio, and on the other is the doorway to the foyer."))
    print("\n1) Go to the foyer")
    print("2) Go to the bathroom")
    print("3) Go the the star room")
    print("4) Go to the mudroom")
    print("5) Go to the kitchen")
    print("6) Go to the study")

    options = ("1", "2", "3", "4", "5", "6")
    choice = get_choice(options)

    if choice == "1":
        foyer()
    elif choice == "2":
        bathroom()
    elif choice == "3":
        star_room()
    elif choice == "4":
        mudroom()
    elif choice == "5":
        kitchen()
    elif choice == "6":
        study()


def bathroom():
    print(fill("\nThe bathroom is tastefully decorated. The bar of soap is shaped like a seashell."))
    print("\n1) Take the soap")
    print("2) Go back to the hallway")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        print("Ew, why would you take old soap? Absolutely not.")
        bathroom()
    elif choice == "2":
        hallway()


def star_room():
    print(fill("The star room is a second bedroom. It has walls painted blue, and was clearly not used much, even before your uncle disappeared."))
    print("1) Go back to the hallway")

    options = ("1")
    choice = get_choice(options)

    if choice == "1":
        hallway()


def study():
    global data
    print("The study was your uncle's main studio, as well as office. It still has an easel with a canvas on it, covered with a paint-splattered cloth. The desk has a few papers on it, and there were two large bookshelves behind it. ")
    print("1) Look at the painting")
    print("2) Look at desk")
    print("3) Go back to the hallway")

    if "dagger" in data["inventory"] and "horrible_painting" not in data["inventory"]:
        print("4) Cut down the painting")
        options = ("1", "2", "3", "4")
        choice = get_choice(options)
    else:
        options = ("1", "2", "3")
        choice = get_choice(options)

    if choice == "1":
        if data["painting"] == False:
            print(fill("You carefully take the cloth off the canvas. The subject is a terrible, beautiful woman, looking straight at you. Her eyes were so entrancing..."))
            for _ in range(30):
                print("........")
                time.sleep(2)

            print(fill("You tear your eyes away from the painting, shaking and sweating. Your heart pounds against your ribs, and you shakily pull the cloth back over the painting. You never want to see it again."))
            data["painting"] = True
        else:
            print(fill("You stare at the cloth-covered canvas and your hands start to shake. You don't want to see that again..."))
            study()
    elif choice == "2":
        print(fill("The desk has many sketches on it, mostly incomplete figure and nature studies. You look through the drawers and find one complete sketch of a horribly lovely woman, her back to the viewer and glancing over her shoulder with a predatory smirk. You shudder, fold the sketch, and put the picture in your pocket."))
        items = {"desk_sketch" : "A folded sketch of a horrible, lovely woman."}
        update_inv(items)
        data["works"] += 1
        study()
    elif choice == "3":
        hallway()
    elif choice == "4":
        print(fill("You take out the rusty dagger. Your hand shakes as you start towards the painting. You are unwilling to take off the cloth again, so you go around to the back of the canvas. You take down the canvas and set it face down on the floor before cutting the painting away from the frame.\n\nAs you cut, your hands begin shaking. A horrible pressure starts against your ears, feeling like a scream against your ears. You work through the pain, and finally manage to cut away the painting. You quickly fold the canvas, taking care to keep the horrible picture inside."))
        items = {"horrible_painting" : "Roughly folded canvas, of the entrancing painting in the study"}
        update_inv(items)
        data["works"] += 1
        study()


def closet():
    print("\nIt's a closet. The coats smell sligtly musty.")
    print("\n1) Rummage through the pockets")
    print("2) Close the door")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":

        if "closet_sketch" in data["inventory"]:
            print(fill("You find some lint, a pencil, and a nickel in the coat pockets."))
            foyer()
        else:
            print(fill("You smooth out the paper. It's a note, with a sketch of a face in profile.\nShe is lovely."))
            items = {"closet_sketch" : "A sketch of a woman."}
            update_inv(items)
            data["works"] += 1
            foyer()
    elif choice == "2":
        foyer()



def mudroom():
    global data
    print(fill("\nThe mudroom has an old washer and dryer, and a set of shelves. The door to the back patio has a set of curtains hanging over the window. Old boots with dried mud sat under a bench beside the door, and an weathered jacket hung on a peg. "))
    print("\n1) Check the shelves")
    print("2) Go through the back door")
    print("3) Go to the hallway")

    options = ("1", "2", "3")
    choice = get_choice(options)

    if choice == "1":
        if "lantern" in data["inventory"]:
            print(fill("\nThe shelves have old laundry products and garden tools."))
            mudroom()
        else:
            shelves()
    elif choice == "2":
        if data["back_door"] == False:
            print(fill("You unlocked the back door to go through."))
            data["back_door"] = True
            patio()
        else:
            patio()
    elif choice == "3":
        hallway()


def shelves():
    print(fill("\nThe shelves have old laundry products and some garden tools. On one shelf is a battery-powered lantern and spare batteries."))
    print("\n1) Take the lantern")
    print("2) Turn back to the mudroom")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        print(fill("You put the new batteries in the lantern and check the light. It turns on and it's pretty bright. You now have a working lantern!"))
        items = {"lantern" : "A lantern"}
        update_inv(items)
        mudroom()
    elif choice == "2":
        mudroom()


# ======   Areas associated with Shed   ======


def shed_door():
    print(fill("The shed is weathered, but sturdy. The door is painted a cheerful red. There are stumps on either side of the door, like there may have been shrubs here at some point. "))
    if data["treehouse"] == True:
        print(fill("Looking to the side, you can see where the path is hidden behind an overgrown bush."))
    print("1) Go into the shed")
    print("2) Go to the front yard")

    if data["treehouse"] == True:
        print("3) Go down the path")
        options = ("1", "2", "3")
        choice = get_choice(options)
    else:
        options = ("1", "2")
        choice = get_choice(options)

    if choice == "1":
        if "red_door_key" in data["inventory"]:
            shed()
        else:
            print("The door is locked.")
    elif choice == "2":
        front_yard()
    elif choice == "3":
        treehouse_path()


def shed():
    print(fill("The shed is dark. The door behind you lets in a little light, but the only other light is a small line of light outlining a small window on the other side of the building.. You struggle to see through the gloom."))
    print("1) Go into the room")
    print("2) Leave the shed")

    if "lantern" in data["inventory"]:
        light_shed()
    else:
        print(fill("You go in a few steps and can't see any better. You retreat to the door. If only there was light..."))
        shed()


def light_shed():
    global data
    print(fill("You turn on the lantern. The shed is clearly an art workshop. There are a couple of windows you can see, but they've all been boarded up except for two. One at the back has a window air conditioner, though it's off for now. The other window not boarded up has a fabric windowshade pulled down over it. Art supplies litter the shed. A pegboard with various tools takes up one long wall, and a sturdy table sits along the back wall. You didn't realize your uncle did wordworking, but the wood shavings on the floor tell another story. Some paint brushes and easels lay in palces."))
    print("1) Open the shade")
    print("2) Leave the shed")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        print(fill("Light trickles in as you open the shade. It doesn't want to stay open. It's on the wall facing away from the driveway and you can see mostly just trees, with a little bit of the back yard. But you also see a path into the trees that hadn't been visible..."))
        if data["treehouse"] == False:
            data["treehouse"] = True
        light_shed()
    elif choice == "2":
        shed_door()



def treehouse_path():
    print(fill("The path goes just a dozen feet into the trees, before ending at the trunk of one large tree. There are wooden slats nailed to the trunk. Looking up, you see a treehouse tucked into the branches."))
    print("1) Climb the ladder")
    print("2) Go to the shed")

    options = ("1", "2",)
    choice = get_choice(options)

    if choice == "1":
        if data["tarp"] == False:
            treehouse_first()
        else:
            treehouse()
    elif choice == "2":
        shed_door()



def treehouse_first():
    print(fill("The treehouse is small, but nice. There's a lump in the corner under a tarp which is weighed down with stones. There are a couple of windows looking out."))
    print("1) Look out the window")
    print("2) Move the tarp")

    options = ("1", "2",)
    choice = get_choice(options)

    if choice == "1":
        print(fill("Out the window, you can just make out the patio behind the house as well as the roof. Looking down, you can make out a faint line of bare dirt completely circling the treehouse. Curious..."))
        if data["tarp"] == False:
            treehouse_first()
        else:
            treehouse()
    elif choice == "2":
        print(fill("You move the stones and the tarp. Underneath is an old footlocker. There is no lock on it, but it looks well-used."))
        locker_first()



def locker_first():  # TODO Figure out how to print the letter again and go back to the room you came from. 
    print(fill("You open the locker. Inside, there's a letter with your name on it. Beneath that is an odd collection of things. Books on fairy lore, closed boxes, odd crystals, an odd variety of items with no obvious purpose."))
    print("1) Read the letter")
    print("2) Open the boxes")
    print("3) Close the locker")

    options = ("1", "2", "3",)
    choice = get_choice(options)

    if choice == "1":
        letter()
    elif choice == "2":
        boxes()
    elif choice == "3":
        treehouse()


def letter():
    print(fill("You open the letter and read.\n\n\n\"I hope you never have to read this, as it will mean I've failed. But if I fail, you're my only hope. I should start at the beginning, but I must keep this brief. There's not much time left before she comes to collect. \n\nAbout a year ago I met a woman at a park. I had taken my supplies out to paint the scenery and became swept up in the inspiration I felt in that spot. When I dragged my focus out of my art, she was there watching me. She was lovely in a way I had never seen, all sharp edges and too-bright colors. I have a difficult time remembering much of the month after that, just flashes of color and emotions too sharp to be natural. I was with her constantly, it seemed.\n\n Finally she left me alone for a day or two and I returned to myself, recalling some of what I had experienced. Long story short, I discovered that the Fae do exist. She is, roughly, a noble in the Seelie Court. While they are known for being kind to us mortals, they are also known for finding artists and inspiring them. This sounds lovely at first, but it is an inspiration that is all-consuming. I have painted until I cannot see straight. I believe there were days when I did not sleep or eat, overcome with the need to put my thoughts to canvas or paper. She consumes me as she inspires. The glamour of the Fae fades with time, but it is also an addiction. Alone now, I cannot think to hold a brush or pencil, my mind craves the rush she inspired. It is hateful.\n\nI have made a deal with her, in my furour. I recalled it after the fact. The Fae, if you recall from when we read fairy tales when you were younger, are bound by their words. They cannot lie, and if they make a deal, they cannot break it. They are creatures of magic and the magic cannot lie. My deal is this: my art made by her inspiration will endure one hundred years after I am gone, a lasting legacy. As long as my legacy endured through my art, I will serve her as a hound for the Wild Hunt. Looking back on it, I found the loophole and I need your help to exploit it. Burn my work. The inspired works are all of her, as the Fae are vain and she wished to be my subject. There are five works devoted to her, you will know them when you see them. I cannot look at them without losing myself again. There are two in frames, they will resist being taken down without help. I've found an iron dagger to leave you and have packed it in a box for the locker. Use that. Iron is poison to them, and cancels their magic. There is a box included with iron cuffs and an iron necklet. I thought to wear them myself, but they will not help me now that I have made my deal. I hope she does not take notice of you, but they may be helpful if she does. \n\nOnce you have my works, burn them with the herbs I have also included. Fire and herbs are enough to break the glamour she has cast and let the works burn. Once they are gone, she will have to release me. The treehouse should be safe from her. I have buried iron bars in an unbroken circle around the tree, she cannot pass the line. It did me no good, but it may help you if the worst comes to pass and she finds you. \n\nBe careful. She is crafty and you will want to follow her lead. Do not let her hounds get you, they, and I, only follow her, and will tear you apart at her command. Only predators are part of the Wild Hunt, and she is a predator. The hounds are an extension of her. \n\nFree me, I beg you. I did not mean for this to happen.\"\n\n"))
    print("1) Close letter")

    options = ("1")
    choice = get_choice(options)

    if choice == "1":
        if "herbs" in data["inventory"]:
            locker()
        else:
            locker_first()

def locker():
    print(fill("You open the locker. The letter sits on the top There is an odd collection of things. Books on fairy lore, odd crystals, an odd variety of items with no obvious purpose."))
    print("1) Read the letter")
    print("2) Close the locker")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        letter()
    elif choice == "2":
        treehouse()


def boxes():
    global data
    print(fill("You open the boxes. They have an odd assortment of items. One contains just dried herbs and flowers, one has a set of metal wrist cuffs and a torque of the same metal. Another has a dagger, the blade flecked with rust."))
    print("1) Take the items")
    print("2) Look through the rest of the locker")

    options = ("1")
    choice = get_choice(options)

    if choice == "1":
        items = ({"dagger" : "A rusty iron dagger."}, {"herbs" : "It's a box of herbs, to burn with the works."})
        update_inv(items)
        data["cuffs"] = True
        print(fill("You put on the cuffs and torque. They sit heavy and cold on your skin. You take the dagger and box of herbs."))
    elif choice == "2":
        if data["cuffs"] == True:
            locker()
        else:
            locker_first()



def treehouse():
    print(fill("The treehouse is small, but nice. There's an old footlocker against one wall. There are a couple of windows looking out."))
    print("1) Look out the window")
    print("2) Look in the footlocker")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        print(fill("Out the window, you can just make out the patio behind the house as well as the roof. Looking down, you can make out a faint line of bare dirt completely circling the treehouse. Curious..."))
    elif choice == "2":
        if "herbs" in data["inventory"]:
            locker()
        else:
            locker_first()



# ======   Areas associated with Back Yard   ======


def path_split():
    print(fill("\nYou see a gazebo on the left and a patio to the right.\n"))
    print("\n1) Go to the gazebo")
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
    print(fill("\nYou enter the gazebo. It's nice, if run down. There are flower boxes along the outside, but they've been empty for years."))
    print("\n1) Go back to the path")
    print("2) Check the flower boxes")
    options = ("1", "2")
    choice = get_choice(options)
    if choice == "1":
        path_split()
    elif choice == "2":
        print("\nThe boxes certainly are empty.\n")
        gazebo()


def patio():
    print(fill("\nThe patio is stone, though there are weeds pushing through the cracks. There's an old fountain to one side, maybe it was once lovely, but now it's covered in grime and moss. The opposite side of the patio has a covered fire pit, the stones have held up fairly well, but a few have fallen down. In the middle of the patio is a rusty set of chairs and a small cafe table, overlooking the overgrown back yard. There is a door into the house on the patio as well. "))
    if data["treehouse"] == True:
        print(fill("\nNow that you know what to look for, you can see the hint of the path to the treehouse out behind the shed."))
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
    print(fill("\nCloser up, the fountain isn't quite as grimy as you thought, but it's still got muck built up at the bottom. Most of the discoloration is just some nice, soft moss covering the stone. "))
    
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
    print(fill("\nThe table is pretty rusty, and so are the chairs. Some of the bars look loose.."))
    print("\n1) Check the bars")
    print("2) Go back to the patio")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        if "rusty_bar" in data["inventory"]:
            print("There are no more loose bars.")
            table()
        else:
            print(fill("\nYou wiggle some of the bars and one breaks off in your hand. You now have a rusty bar. You try to remember when you had your last tetanus shot..."))
            items = {"rusty_bar": "A rusty iron bar. When did you have your last tetanus shot..."}
            update_inv(items)
            table()
    elif choice == "2":
        patio()


def fire_pit():
    print(fill("The fire pit is a half-sphere of stone, with some of the bricks missing from the structure. A few of these are in the center of the pit. "))
    print("1) Turn back to the patio")

    if data["works"] == 5:
        print("2) Burn the works")
        options = ("1", "2")
        choice = get_choice(options)

    options = ("1")
    choice = get_choice(options)

    if choice == "1":
        patio()
    elif choice == "2":
        save()
        if "herbs" in data["inventory"]:
            burn()
        else:
            bad_burn()


def back_door():
    print(fill('The door is faded blue, and there is an old mat that says "Oh, it\'s you..."'))
    print("1) Go through the door")
    print("2) Check under the mat")
    print("3) Go back to patio")
    
    options = ("1", "2", "3")
    choice = get_choice(options)

    if choice == "1":
        if "blue_door_key" in data["inventory"]:
            mudroom()
        else:
            print("The door is locked...")
            back_door()
    elif choice == "2":
        if "blue_door_key" in data["inventory"]:
            print("There's nothing else under here.")
            back_door()
        else:
            print(fill("You now have a small metal key! It's too small for a door..."))
            items = {"mailbox_key" : "A small metal key."}
            update_inv(items)
            back_door()
    elif choice == "3":
        patio()



#   ======   Endgame functions   ======


def burn():
    global data
    print(fill("You pile all five of your uncle's glamored works into the fire pit and dump the herbs on top. Then you strike a match and hold it to one of the sketches. The flames catch and, slowly, they begin to spread. The flames seem to move slower than normal, until one of the herbs catches. As that happens, the flames seem to roar, growing and moving faster. \n\nYou hear hounds baying in the distance... Are they getting closer?"))
    print("1) They're definitely getting closer. Run to the treehouse.")
    print("2) Stay where you are. It's probably nothing..")

    options = ("1", "2")
    choice = get_choice(options)
    data["burned"] = True

    if choice == "1":
        treehouse_run()
    elif  choice == "2":
        firepit_stand()


def bad_burn():
    print(fill("You pile all of your uncle's glamored works into the fire pit. You hesitate for a moment. Wasn't there something else you need to add...?"))
    print("1) No, this seems right, burn them")
    print("2) This is wrong, gather the paintings and keep looking around...")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        firepit_choice()
    elif choice == "2":
        patio()


def firepit_choice():
    print(fill("You strike a match and hold it to one of the sketches. The flame catches, finally, and slowly begins to spread. The flames move slower than usual, and don't move to the center of any of the works. Even the sketches on dry paper don't do more than curl at the edges. The flames begin to die out, and in the distance, you begin to hear hounds baying...."))
    print("1) Run to the treehouse")
    print("2) Stand your ground")

    options = ("1", "2")
    choice = get_choice(options)

    if choice == "1":
        treehouse_run()
    elif choice== "2":
        firepit_stand()


def firepit_stand():
    global data
    print(fill("You begin to shake as hounds appear as if from nowhere. They are red and white and huge, and they circle around you, hackles up and teeth bared. But the worst of it is the woman. You don't see her approach, she just suddenly is there in front of you. She is horribly lovely, and much too close. She smiles. \"Meddlesome,\" she says. Her voice seeps into you and you relax, smiling. She looks at the slightly sooty art in the firepit and seems amused.\n\"You have caused me some irritation, child. But I see no lasting harm has been done.\"\nShe looks back at you, smile growing to show too many teeth.\n\"Now then, come, join my pack.\" Her hand reaches out to you."))
    while True:
        choice = input("Press Enter to continue")

        if choice == "":
            if data["cuffs"] == True:
                print(fill("Heat has been building on your hands and wrists, and now it reaches an uncomfortable level, almost burnig. You jolt away from her reaching hand, stumbling back from her. She still seems amused as you turn and begin to run. A laugh sounds out behind you as you hear the easy command.\n\"Hunt.\"\n\nGrowls and panting sounds behind you. You run."))
                data["end"] = "worst"
            else:
                print(fill("You step towards her hand, eager to serve, and she laughs. You feel a shiver over your skin as your body begins to change. But she is still laughing, and you trust she will do what is best for you. Your tail begins to wag as she reaches down to put a hand on your head. Your Lady loves you, and you begin to run with your pack as she leads you into the Fae Wild."))
                data["end"] = "hound"


def treehouse_run():
    print(fill("You take off at a run towards the treehouse, it's not far, you should be fine. The baying continues to sound closer as your feet hit the path. They sound faster than they have any right to be. As you round the last turn towards the treehouse, a crash sounds behind you and you hear growls and snarls behind you. You don't look back, running across the faint line in the dirt around the treehouse and slamming into the tree trunk, scrambling around to get to the ladder. You glance behind you as you fumble on the ladder slats, and you stop completely.\n\n"))

    if data["burned"] == True:
        while True:
            choice = input("Press Enter to continue")
            if choice == "":
                treehouse_end()
    else:
        treehouse_bad()


def treehouse_bad():
    global data
    print(fill("The hounds are white and red, and huge. They've slammed to a halt at the line in the dirt, and are starting to circle around. The woman is also there. She is horribly lovely, and she is staring right at you.\n\n\"Hello, child.\"\nHer voice rocks through your mind, wiping away the adrenaline and panic, leaving only a lovely calm. She smiles at you and it is the most wonderful thing you have ever seen. You smile back, content.\n\n\"You are a troublesome child,\" she says. You shudder at her displeasure. \"You may as well come out of there.\""))
    while True:
        choice = input("Press Enter to continue")

        if choice == "":
            if data["cuffs"] == True:
                print(fill("Heat has been building on your hands and wrists, and now it reaches an uncomfortable level, almost burnig. Her hold on you slips and you shake your head and step back.\n\"Give me my uncle,\" you say. She throws her head back and laughs, making a chill go down your spine.\n\"Why would I do such a thing?\" she laughs. \"He and I had a deal, and it is still in force.\" One of the hounds sits at her side, and she lays a proprietary hand on its head.\n\"And he has been such a good hound. Won't you come join him?\"\nHorrified, you shake you head mutely. She shrugs. \"Oh well, come along boys. I had better pick up those lovely pieces of art on our way back. We wouldn't want this happening again...\"\n\nYou can only watch, numb, as she turns and walks out into the woods, hounds following along behind.\n\nIt's a long time before you can make yourself move again."))
                data["end"] = "bad"
                finish()


def treehouse_end():
    print(fill("The hounds are white and red, and huge. They've slammed to a halt at the line in the dirt, and are starting to circle around. The woman is also there. She is horribly lovely, and she is staring right at you.\n\n\"Hello, child.\""))

    while True:
        choice = input("Press Enter to continue")
        global data
        if choice == "":
            print(fill("Her voice rocks through your mind, wiping away the adrenaline and panic, leaving only a lovely calm. She smiles at you and it is the most wonderful thing you have ever seen. You smile back, content.\n\n \"You have done so much here,\" she says in a lilting voice. \"Your loyalty to your uncle is quite admirable. You would make a wonderful hound for me with such devotion.\" You think that her smile has maybe too many teeth...\n\n"))
            if data["cuffs"] == True:
                print("Heat has been building on your wrists and neck as you stared at her, and now it reaches an uncomfortable level, almost burning. You realize whatever hold she had on you is slipping and you take a step back, shaking your head to wake up more.\n\"No,\" you say, \"I've destroyed the art you made a deal about, now give back my uncle.\"\n\nHer face twists into a vicious snarl.\n\"You have cost me a hound, child. It would be better for you if you agreed to replace him.\"\n\n\"I have no deals with you, and the terms of his deal have been broken,\" you say. \"Give me back my uncle.\"")
                end_best()
            else:
                print("Her eyes are the most entrancing thing you've ever seen, and her voice is captivating. You take a step forward and she smiles. You want to make her happy, you would do anything. So you walk forward and over the line in the dirt. She laughs, and you laugh, too. You know she'll take care of you. You feel a shiver over your skin as your body begins to change. But she is still laughing, and you trust she will do what is best for you. Your tail begins to wag as she reaches down to put a hand on your head. Your Lady loves you, and you begin to run with your pack as she leads you into the Fae Wild.")
                data["end"] = "hound"



def end_best():
    choice = input("Press Enter to continue")
    global data
    data["end"] = "best"
    if choice == "":
        print(fill("The sound she makes is horrible, a scream of rage so intense the hounds begin to howl. Your vision begins to shake, so you shut your eyes and clamp your hands over your ears. It continues for another few moments, then abruptly cuts off, leaving an echo in the air. You cautiously let down your hands and open your eyes. The woman is gone, as are all but one of the hounds. It sits right outside the circle, its head tilted. As it sees you looking, its tail stards to wag.\n\nYou slowly walk towards it. Uncertain, you pause, and take the torque off your neck. You slowly walk out of the circle, ready to jump back if the animal lunges, but it just wags its tail faster. You lower the torque, and place it gently around the dog's neck."))
        time.sleep(10)
        print(fill("The hound shakes itself after a few moments, then whines and paws at the torque. It yelps once, making you flinch back into the circle. But when you look back, the hound is gone. Your uncle is sitting on the ground with the torque around his neck, staring at his hands and grinning."))
        time.sleep(10)
        finish()


def finish():
    print("\n\n\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("================================")
    print("-----------Inheritance----------")
    print("================================")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if data["end"] == "best":
        print(fill("Congratulations! You discovered the secrets of your uncle's disappearance and were able to rescue him from the Fae woman."))
    elif data["end"] == "hound":
        print(fill("You were so close to victory, but you were missing some things. Oh well, at least life should be easy as a hound. Maybe you can do better if you try again? Good luck!"))
    elif data["end"] == "bad":
        print(fill("It's too bad the art didn't burn. Maybe there was something more to be done for it? Well, hopefully she won't be back, but you've lost your uncle permanently this time. Maybe you can try again and figure out some more secrets? I'm sure you'll do better next time."))

    print(fill("Thank you for playing Inheritance, an investigation adventure by MG Marlowe."))


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
    "cuffs" : False,
    "painting" : False,
    "treehouse" : False,
    "front_door" : False,
    "back_door" : False,
    "tarp" : False,
    "mailbox" : False,
    "inventory" : {},
    "works" : 0
}

load()
