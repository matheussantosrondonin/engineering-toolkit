# ==========================================================
# Project: Engineering Toolkit
# Description: length conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================


#==========================================================
# importing the necessary modules
#==========================================================
from conversion_math import from_meter, to_meter
from utils import show_length_units, show_result_box
from config import length_units
#==========================================================



def length_converter():

    #menu for length conversion
    show_length_units()

    #choose source unit
    source_unit_choice = input("\nPlease select a length unit by entering the corresponding number: ")

    if source_unit_choice == "5":
        print("Returning to conversion types menu.")
        return  #end actual function and return control to the caller of this function.

    #validation of source unit choice
    if source_unit_choice in length_units:
        source_unit = length_units[source_unit_choice]
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

    show_length_units()

    #validation of target unit choice
    target_unit_choice = input("\nNow, please select the second length unit for conversion:\n")
    if target_unit_choice == "5":
        print("Returning to conversion types menu.")
        return  #end actual function and return control to the caller of this function.

    #validation of target unit choice
    if target_unit_choice in length_units:
        target_unit = length_units[target_unit_choice]

        value_in_meters = to_meter(conversion_value, source_unit)
        result = from_meter(value_in_meters, target_unit)

        # Formata o resultado final (int ou float com até 4 casas)
        length_result = int(result) if result.is_integer() else round(result, 4)

        # Monta a string do resultado
        text_result = f"{result_display} {source_unit} is equal to {length_result} {target_unit}"

        # Display the result in a formatted box
        show_result_box(text_result)

    else:
        print("Invalid target unit selection.")
