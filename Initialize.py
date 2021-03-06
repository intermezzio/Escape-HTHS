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
Bandaid2 = Item("bandaid", -4, "Covers up those locker cuts. Heals 4 points of damage when used. Permanently disappears after use.")
Bandaid3 = Item("bandaid", -4, "Covers up those locker cuts. Heals 4 points of damage when used. Permanently disappears after use.")
Bandaid4 = Item("bandaid", -4, "Covers up those locker cuts. Heals 4 points of damage when used. Permanently disappears after use.")
Backpack = Item("backpack", 0, "A larger backpack. Can hold 10 items instead of 5.")

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
Rm185Floor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# 155 Storage
##
BioDesk = Storage("desk", 2, [SafetyRules], "Approach the desk", "There are a few biology worksheets.")
BioCloset = Storage("closet", 4, [Apron], "Open the door to the closet", "You look inside the closet. Everything is neatly organized.")
BioFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# Tech Lab Storage
##
TechCabinet = Storage("cabinet", 3, [], "Open the cabinet", "You open the cabinet. Inside are various tools.", key = "special tech")
TechFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# Chem Lab Storage
##
ChemCabinet = Storage("cabinet", 3, [MainKey], "Open the cabinet", "You open the cabinet. Inside are rows of beakers and Erlenmeyer flasks, along with some chemicals.", key = "special chem")
ChemFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# Main Office Storage
##
OfficeDesk = Storage("desk", 2, [Bandaid3], "Open the cabinet", "You open the cabinet. Inside are many files and folders.", key = "special main")
OfficeFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# Nurse's Office Storage
##
NurseCabinet = Storage("cabinet", 3, [Bandaid, Bandaid2], "Open the cabinet", "You open the cabinet. Inside are some first aid tools.")
NurseFloor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# 125 Storage
##
Rm125Closet = Storage("closet", 2, [Backpack], "Open the closet", "You open the closet. Inside are various items.")
Rm125Floor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")

##
# 180 Storage
##
Rm180Floor = Storage("floor", 100, [], "See what's on the floor", "The floor is dirty.")
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
CSE = Room("Mr. Hanas' Room", "170", [CSEBin, CSEFloor], "You enter room 170 again. Mr. Hanas glances at you from his desk. The impossible Python assignment is still on the computer that you were using earlier.", specialActions = {"program":"Keep trying to program the impossible Python assignment"}, NPCs = Hanas)
Rm185 = Room("Ms. G's Room", "185", [Rm185Desk, Rm185Closet, Rm185Floor], "You enter Room 185. Hanging on the wall is a sign that says \"Ms. G\'s Room.\" There are several student desks in the center of the room, and desktop computers lining the walls. In the front of the room is Ms. G\'s desk with several items on it, as well as two doors.", specialActions = {})
Bio = Room("Mr. Roche's Room", "155", [BioDesk, BioCloset, BioFloor], "You enter Room 155. There are a few sheets of paper on the student desk near the door and a closet in the back. The skeleton at the far end of the room stares into your soul.", specialActions = {"skeleton":"Approach the skeleton"})
TechLab = Room("Tech Lab", "tech", [TechCabinet, TechFloor], "You enter the tech lab. There are some wood scraps on the work tables and multiple closets and cabinets along the walls.", specialActions = {}, light=False, lock="tech lab key")
ChemLab = Room("Chem Lab", "140", [ChemCabinet, ChemFloor], "You enter the chem lab. All lab equipment is cleaned and stored in the cabinets. Ms. Pannapara stands in the doorway to her prep room.", specialActions = {"prep":"Approach the prep room"}, NPCs = None)
MainOffice = Room("Main Office", "main", [OfficeDesk, OfficeFloor], "You enter the main office. Mr. Bals (20 HP) immediately comes out of his personal office.", specialActions = {}, NPCs = Bals, lock="main office key")
NurseOffice = Room("Nurse's Office", "nurse", [NurseCabinet, NurseFloor], "You enter the nurse\'s office. Next to Mrs. Finley's desk there is a cabinet. In the corner there is a bed.", specialActions = {"sleep":"Sleep on the bed"}, NPCs = None)
Rm125 = Room("Mrs. LeBlanc's Room", "125", [Rm125Closet, Rm125Floor], "You enter room 125. There is a closet near the door. Suddenly, black lines (10 HP) swarm out of a math textbook.", specialActions = {}, NPCs = Mob)
Rm180 = Room("Mr. B's Room", "180", [Rm180Floor], "You enter room 180. Mr. B (10 HP) sits behind his computer. Stay Honest In Testing devices are on the shelf.", specialActions = {}, NPCs = Borchardt)