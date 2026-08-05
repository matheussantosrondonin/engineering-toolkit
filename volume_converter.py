# ==========================================================
# Project: Engineering Toolkit
# Description: Volume conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================


#==========================================================
# importing the necessary modules
#==========================================================

from conversion_math import to_liters, from_liters
from utils import show_volume_units, show_result_box
from config import volume_units

#=========================================================

def volume_converter():
    #menu for volume conversion
    show_volume_units()

    #choose source unit
    source_unit_choice = input("\nPlease select a volume unit by entering the corresponding number: ")

    if source_unit_choice == "5":
        print("Returning to conversion types menu.")
        return  #end actual function and return control to the caller of this function.

    #validation of source unit choice
    if source_unit_choice in volume_units:
        source_unit = volume_units[source_unit_choice]
        print(f"You selected {source_unit}.")

    else:
        print("Invalid choice.")
        return

    #validation of conversion value
    conversion_value_input = input("\nPlease enter a value: ")
    try:
        conversion_value = float(conversion_value_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    result_display = int(conversion_value) if conversion_value.is_integer() else round(conversion_value, 4)
    print(f"You entered: {result_display} {source_unit}")

    print("\npress enter to continue...")
    input()  # Wait for user to press Enter

    show_volume_units()

    #validation of target unit choice
    target_unit_choice = input("\nNow, please select the second volume unit for conversion:\n")
    if target_unit_choice == "5":
        print("Returning to conversion types menu.")
        return  #end actual function and return control to the caller of this function.

    if target_unit_choice in volume_units:
        target_unit = volume_units[target_unit_choice]

        value_in_liters = to_liters(conversion_value, source_unit)
        result = from_liters(value_in_liters, target_unit)

        # Formata o resultado final (int ou float com até 4 casas)
        volume_result = int(result) if result.is_integer() else round(result, 4)

        # Monta a string do resultado
        text_result = f"{result_display} {source_unit} is equal to {volume_result} {target_unit}"
        show_result_box(text_result)

    else:
        print("Invalid choice.")
