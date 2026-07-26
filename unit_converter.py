# ==========================================================
# Project: Engineering Toolkit
# Description: Unit conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

#==========================================================
# importing the necessary modules
#==========================================================

from config import list_of_conversion_types, list_of_pressure_units
from pressure_converter import pressure_converter
from utils import show_converter_header

# ==========================================================
# Menu for the Unit Converter
# ==========================================================

def unit_converter():
    show_converter_header()
    print("\nAvailable conversion types:\n")
    for conversion_type in list_of_conversion_types:
        print(f"  {conversion_type}")
    
    # 1. Escolha do tipo de conversão (ex: Pressão, Temperatura...)
    menu_choice = input("\nPlease select a conversion type by entering the corresponding number: ")

    # ==========================================================
    # Choose pressure conversion (Opção 1)
    # ==========================================================
    while menu_choice not in ["1", "2", "3", "4", "5", "6"]:
                print("Invalid option. Please try again.")
                menu_choice = input("\nPlease select a conversion type by entering the corresponding number: ")
            
    if menu_choice == "1":
        pressure_converter()


    if menu_choice == "6":
        print("Returning to main menu.")
        return  #encerra a função atual e devolve o controle para quem chamou essa função.

        
        
        

    
    # You can add functions for converting pressure, temperature, length, mass, and volume

# ==========================================================




