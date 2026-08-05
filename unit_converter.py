# ==========================================================
# Project: Engineering Toolkit
# Description: Unit conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

#==========================================================
# importing the necessary modules
#==========================================================

from length_converter import length_converter
from pressure_converter import pressure_converter
from utils import show_conversion_types
from temperature_converter import temperature_converter
from mass_converter import mass_converter
from volume_converter import volume_converter

# ==========================================================
# Menu for the Unit Converter
# ==========================================================

def unit_converter():

    while True:
        show_conversion_types()
    
    # 1. Escolha do tipo de conversão (ex: Pressão, Temperatura...)
        menu_choice = input("\nPlease select a conversion type by entering the corresponding number: ")

    # ==========================================================
    # Choose pressure conversion (Opção 1)
    # ==========================================================
        while menu_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid option. Please try again.")
            menu_choice = input("\nPlease select a conversion type by entering the corresponding number: ")
            
        if menu_choice == "6":
            print("Returning to main menu.")
            return

        if menu_choice == "1":
            pressure_converter()

        elif menu_choice == "2":
            temperature_converter()

        elif menu_choice == "3":
            length_converter()

        elif menu_choice == "4":
            mass_converter()

        elif menu_choice == "5":
            volume_converter()
        




    

        
        
        

    
    # You can add functions for converting pressure, temperature, length, mass, and volume

# ==========================================================




