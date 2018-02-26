# -*- coding: utf-8 -*-
"""
Initialize.py

This file creates all of the objects 
(User, Room, Storage, Item, Function) 
and stores them as variables to be 
accessed in the main method.

"""
from RoomClass import *
from StorageClass import *
from UserClass import *
from ItemClass import *
from NpcClass import *
#from FunctionClass import *

########
# Create Basic Functions
########
f1 = None # default function for everything, will make functions when the class is done


########
# Create Basic Items
########
Die = Item("die", 1, "A twenty-sided die. Left behind by a D&D player.")
Pencil = Item("pencil", 1, "A pencil. Can be used to write, among other uses. A weak weapon.")
Pen = Item("pen", 2, "A pen. Can be used to write smoothly, among other uses. A weak weapon, but stronger than a pencil.")
Frisbee = Item("frisbee", 3, "An orange disc that can fly if thrown properly. A fairly powerful weapon.")
SafetyRules = Item("safety rules", 0, "A list of safety rules for the chem lab and tech lab. I hope you passed your quiz...")
Apron = Item("apron", 0, "A chemical-resistant apron. Must be worn in the chem lab.")
TechKey = Item("tech lab key", 0, "A key that can lock or unlock the door to the tech lab.")
Goggles = Item("goggles", 0, "A pair of goggles. Used for eye protection. Must be worn in the chem lab and in the tech lab.")
Lightbulb = Item("lightbulb", 0, "How many high techers does it take to screw in a lightbulb?")
Calculator = Item("calculator", 10, "A TI-Nspire. It may just be a calculator, but it\'s a very powerful tool. Occasionally a very powerful weapon.")
MainKey = Item("main office key", 0, "A key to the main office.")
Bandaid = Item("bandaid", -4, "Covers up those locker cuts. Heals 4 points of damage when used. Permanently disappears after use.")
Bandaid2 = Bandaid.clone()
Bandaid3 = Bandaid.clone()
Bandaid4 = Bandaid.clone()
Textbook = Item("textbook", 3, "A history textbook. Very heavy and a fairly powerful weapon.")
Acid = Item("acid", 4, "A large bottle of hydrochloric acid. Can only be used once. A dangerous weapon.")

########
# Create Storage
########

##
# CSE Storage
##
CSEBin = Storage("bin", 4, [Pen], "Open the storage bin", "You look inside the bin and find many VEX parts.", key = "special CSE")
CSEFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# 185 Storage
##
Rm185Desk = Storage("desk", 2, [TechKey], "Approach Ms. G\'s desk", "There are a lot of papers on Ms. G\'s desk.") #ms. g's desk
Rm185Closet = Storage("closet", 4, [Goggles, Lightbulb], "Open the door to the closet", "You look inside the closet. A lot of materials are crammed inside of it.")
Rm185Floor = CSEFloor.clone()

##
# 155 Storage
##
BioDesk = Storage("desk", 2, [SafetyRules], "Approach the desk", "There are a few biology worksheets.")
BioCloset = Storage("closet", 4, [Apron], "Open the door to the closet", "You look inside the closet. Everything is neatly organized.")
BioFloor = CSEFloor.clone()

##
# Tech Lab Storage
##
TechCabinet = Storage("cabinet", 3, [Calculator], "Open the cabinet", "You open the cabinet. Inside are various tools.", key = "special tech")
TechFloor = CSEFloor.clone()

##
# Chem Lab Storage
##
ChemCabinet = Storage("cabinet", 3, [MainKey], "Open the cabinet", "You open the cabinet. Inside are rows of beakers and Erlenmeyer flasks, along with some chemicals.", key = "special chem")
ChemFloor = CSEFloor.clone()

##
# 120/130 Storage
##
Rm120Shelf = Storage("shelf", 2, [Textbook], "Approach the shelf", "You look at the shelf. There are many history textbooks on it.")
Rm130Cabinet = Storage("cabinet", 2, [MainKey], "Open the cabinet", "You open the cabinet. Inside are many files and folders.")
Rm120130Floor = CSEFloor.clone()

##
# Main Office Storage
##
OfficeDesk = Storage("desk", 2, [Bandaid3], "Open the cabinet", "You open the cabinet. Inside are many files and folders.", key = "special main")
OfficeFloor = CSEFloor.clone()

##
# Nurse's Office Storage
##
NurseCabinet = Storage("cabinet", 3, [Bandaid, Bandaid2], "Open the cabinet", "You open the cabinet. Inside are some first aid tools.")
NurseFloor = CSEFloor.clone()

##
# 125 Storage
##
Rm125Floor = CSEFloor.clone()

##
# 180 Storage
##
Rm180Floor = CSEFloor.clone()

########
# Create NPCs
########
Hanas = boss("Mr. Hanas", "You see a biker, but it's not just any biker...it's Mr. Hanas!", "roll", 5, [Pencil])
Borchardt = boss("Mr. B", "Standing in front of you is the legendary destroyer of GPA's. Meet Mr. B.", "supercomputer", 10, [Frisbee])
Bals = boss("Mr. Bals", "His affinity for detention has caused many a student much heartache. Meet Mr. Bals.", "detention", 20, [Bandaid4])
Mob = boss("Mob of Calculus Problems", "A terrifying swarm of various multivariable calculus problems has appeared!", "math", 10, [Calculator])

########
# Create Rooms
########
CSE = Room("Mr. Hanas' Room", "170", [CSEBin, CSEFloor], "You enter room 170 again. Mr. Hanas glances at you from his desk. The impossible Python assignment is still on the computer that you were using earlier.", specialActions = {"program":"Keep trying to program the impossible Python assignment"}, NPCs = [Hanas], lock = "defeat boss")
Rm185 = Room("Ms. G's Room", "185", [Rm185Desk, Rm185Closet, Rm185Floor], "You enter Room 185. Hanging on the wall is a sign that says \"Ms. G\'s Room.\" There are several student desks in the center of the room, and desktop computers lining the walls. In the front of the room is Ms. G\'s desk with several items on it, as well as two doors.")
Bio = Room("Mr. Roche's Room", "155", [BioDesk, BioCloset, BioFloor], "You enter Room 155. There are a few sheets of paper on the student desk near the door and a closet in the back. The skeleton at the far end of the room stares into your soul.", specialActions = {"skeleton":"Approach the skeleton"})
TechLab = Room("Tech Lab", "tech", [TechCabinet, TechFloor], "You enter the tech lab. There are some wood scraps on the work tables and multiple closets and cabinets along the walls.", light=False, lock="tech lab key")
ChemLab = Room("Chem Lab", "140", [ChemCabinet, ChemFloor], "You enter the chem lab. All lab equipment is cleaned and stored in the cabinets. Ms. Pannapara stands in the doorway to her prep room.", specialActions = {"prep":"Approach the prep room"}, NPCs = [])
Rm120130 = Room("Mrs. Mannion's and Mrs. Ascari's Room", "120/130", [Rm120Shelf, Rm130Cabinet, Rm120130Floor], "You enter room 120/130. There is a bookshelf next to Mrs. Mannion\'s desk and a black cabinet next to Mrs. Ascari\'s desk.")
MainOffice = Room("Main Office", "main", [OfficeFloor], "You enter the main office. Mr. Bals immediately comes out of his personal office.", NPCs = [Bals], lock="main office key")
NurseOffice = Room("Nurse's Office", "nurse", [NurseCabinet, NurseFloor], "You enter the nurse\'s office. Mrs. Finley is at her desk, next to which there is a cabinet. In the corner there is a bed.", specialActions = {"sleep":"Sleep on the bed"}, NPCs = [])
Rm125 = Room("Mrs. LeBlanc's Room", "125", [Rm125Floor], "You enter room 125. Mrs. LeBlanc walks up from her desks and greets you.", NPCs = [Mob])
Rm180 = Room("Mr. B's Room", "180", [Rm180Floor], "You enter room 180. Mr. B sits behind his computer. Stay Honest In Testing devices are on the shelf.", NPCs = [Borchardt])