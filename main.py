# ==========================================================
# Project: Engineering Toolkit
# Description: Engineering utilities developed during Project Atlas.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

#==========================================================
# importing the necessary modules
#==========================================================

from unit_converter import unit_converter
from pressure_calculator import pressure_calculator
from utils import show_header
from config import separator, author_name

#==========================================================
# Tool Introduction
#==========================================================

show_header()
# import menu for the utils

#==========================================================
# User Interaction name input
#==========================================================

user_name = input("\nPlease enter your name: ")

if not user_name:
    user_name = "User"
if user_name == author_name:
    print("\nHello, Creator Matheus! It's great to see you using your own toolkit!")
else:
    print(f"\nWelcome, {user_name}! Let's explore the Engineering Toolkit together!")

#==========================================================
# Tool Selection menu
#==========================================================

print(separator)
print("Available Tools:")
print("1 - Unit Converter")
print("2 - Pressure Calculator")
print("3 - Exit")
print(separator)

option_tool = input("\nPlease select a tool by entering the corresponding number: \n")

#==========================================================
# Tool Execution based on user selection
#==========================================================

if option_tool == "1":
    unit_converter()
elif option_tool == "2":
    pressure_calculator()
elif option_tool == "3":
    print("Thank you for using the Engineering Toolkit. Goodbye!")
else:
    print("Invalid option. Please try again.")

# alterar para comando from assim que o arquivo unit_converter.py e pressure_calculator.py estiverem prontos
#==========================================================
