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
from utils import show_header, show_tool_menu
from config import author_name

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

show_tool_menu()
option_tool = input("\nPlease select a tool by entering the corresponding number: \n")

#==========================================================
# Tool Execution based on user selection
#==========================================================
while option_tool != "3":
    if option_tool == "1":
        unit_converter()
    
      
    elif option_tool == "2":
        pressure_calculator()

    show_tool_menu()
    option_tool = input("\nPlease select a tool by entering the corresponding number: \n")

while option_tool not in ["1", "2", "3"]:
    print("Invalid option. Please try again.")
    option_tool = input("\nPlease select a tool by entering the corresponding number: \n")

print("\nThank you for using the Engineering Toolkit! Goodbye!")

# alterar para comando from assim que o arquivo unit_converter.py e pressure_calculator.py estiverem prontos
#==========================================================