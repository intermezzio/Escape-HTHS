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
