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
Pencil = Item("Pencil", f1, "A pencil. Can be used to write, among other uses.")
Frisbee = Item("Frisbee", f1, "An orange disc that can fly if thrown properly.")
SafetyRules = Item("Safety Rules", f1, "A list of safety rules for the chem lab and tech lab. I hope you passed your quiz...")
Apron = Item("Apron", f1, "A chemical-resistant apron. Must be worn in the chem lab.")
TechKey = Item("Tech Lab Key", f1, "A key that can lock or unlock the door to the tech lab.")
Goggles = Item("Goggles", f1, "A pair of goggles. Used for eye protection. Must be worn in the chem lab and in the tech lab.")
Lightbulb = Item("Lightbulb", f1, "How many high techers does it take to screw in a lightbulb?")
Calculator = Item("TI-Nspire", f1, "It may just be a calculator, but it’s a very powerful tool.")

########
# Create Storage
########

##
# CSE Storage
##
CSEBin = Storage("Storage Bin", 4, [Pencil.clone(), SafetyRules.clone()], "A drawer in the front of the Mr. Hanas' room.")
# add more storage for CSE here and put it in the array in the Room

##
# Next Room Stuff Here
##

########
# Create Rooms
########
CSE = Room("Mr. Hanas' Room", 170, [CSEBin], "Mr. Hanas' room is ____________________________", NPCs = [])
