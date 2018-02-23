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
#from FunctionClass import *

########
# Create Basic Functions
########
f1 = None # default function for everything, will make functions when the class is done


########
# Create Basic Items
########
Pencil = Item("pencil", 1, "A pencil. Can be used to write, among other uses.")
Pen = Item("pen", 2, "A pen. Can be used to write smoothly, among other uses.")
Frisbee = Item("frisbee", 3, "An orange disc that can fly if thrown properly.")
SafetyRules = Item("safety rules", 0, "A list of safety rules for the chem lab and tech lab. I hope you passed your quiz...")
Apron = Item("apron", 0, "A chemical-resistant apron. Must be worn in the chem lab.")
TechKey = Item("tech lab key", 0, "A key that can lock or unlock the door to the tech lab.")
Goggles = Item("goggles", 0, "A pair of goggles. Used for eye protection. Must be worn in the chem lab and in the tech lab.")
Lightbulb = Item("lightbulb", 0, "How many high techers does it take to screw in a lightbulb?")
Calculator = Item("calculator", 10, "A TI-Nspire. It may just be a calculator, but it’s a very powerful tool.")
MainKey = Item("main office key", 0, "A key to the main office.")
Bandaid = Item("bandaid", 4, "Covers up those locker cuts.")
Bandaid2 = Bandaid.clone()

########
# Create Storage
########

##
# CSE Storage
##
#CSEBin = Storage("Storage Bin", 4, [], "A drawer in the front of Mr. Hanas' room.")

##
# 185 Storage
##
Rm185Desk = Storage("Ms. G's desk", 2, [TechKey], "There are a lot of papers on Ms. G’s desk.")
Rm185Closet = Storage("closet", 4, [Goggles, Lightbulb], "You look inside the closet. A lot of materials are crammed inside of it.")

##
# 155 Storage
##
BioDesk = Storage("desk", 2, [SafetyRules], "There are a few biology worksheets.")
BioCloset = Storage("closet", 4, [Apron], "You look inside the closet.")

##
# Tech Lab Storage
##
TechCabinet = Storage("cabinet", 3, [], "You open the cabinet. Inside are various tools.", key = "special tech")

##
# Chem Lab Storage
##
ChemCabinet = Storage("cabinet", 3, [], "You open the cabinet. Inside are rows of beakers and Erlenmeyer flasks.", key = "special chem")

##
# 130 Storage
##
Rm130Cabinet = Storage("cabinet", 2, [MainKey], "You open the cabinet. Inside are many files and folders.")

##
# Nurse's Office Storage
##
NurseCabinet = Storage("cabinet", 3, [Bandaid, Bandaid2], "You open the cabinet. Inside are some first aid tools.")

########
# Create Rooms
########
CSE = Room("Mr. Hanas' Room", "170", [], "You enter room 170 again. Mr. Hanas glances at you from his desk. The impossible Python assignment is still on the computer that you were using earlier.", NPCs = [])
Rm185 = Room("Ms. G's Room", "185", [Rm185Desk, Rm185Closet], "You enter Room 185. Hanging on the wall is a sign that says “Ms. G’s Room.” There are several student desks in the center of the room, and desktop computers lining the walls. In the front of the room is Ms. G’s desk with several items on it, as well as two doors.")
Bio = Room("Mr. Roche's Room", "155", [BioDesk, BioCloset], "You enter Room 155. There are a few sheets of paper on the student desk near the door and a closet in the back. The skeleton at the far end of the room stares into your soul.")
TechLab = Room("Tech Lab", "tech", [TechCabinet], "You enter the tech lab. There are some wood scraps on the work tables and multiple closets and cabinets along the walls.", light=False, lock="tech lab key")
ChemLab = Room("Chem Lab", "145", [ChemCabinet], "You enter the chem lab. All lab equipment is cleaned and stored in the cabinets. Ms. Pannapara stands in the doorway to her prep room.", NPCs = [])
Rm120 = Room("Mrs. Mannion's Room", "120", [], "You enter room 120. Room 130 is blocked off by the divider.")
Rm130 = Room("Mrs. Ascari's Room", "130", [Rm130Cabinet], "You enter room 130. There is a black cabinet next to Mrs. Ascari’s desk.", lock="no key")
MainOffice = Room("Main Office", "main", [], "You enter the main office. Mr. Bals immediately comes out of his personal office.", NPCs = [], lock="main office key")
NurseOffice = Room("Nurse's Office", "nurse", [NurseCabinet], "You enter the nurse’s office. Mrs. Finley is at her desk, next to which there is a cabinet. In the corner there is a bed.", NPCs = [])
Rm125 = Room("Mrs. LeBlanc's Room", "125", [], "You enter room 125. Mrs. LeBlanc walks up from her desks and greets you.", NPCs = [])