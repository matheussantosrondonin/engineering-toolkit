# ==========================================================
# Project: Engineering Toolkit
# Description: Temperature conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================


#==========================================================
# importing the necessary modules
#==========================================================

from utils import show_temperature_units
from conversion_math import (to_celsius, from_celsius)

#==========================================================

def temperature_converter():
    #menu for temperature conversion
    show_temperature_units()

    #choose temperature unit
    source_unit_choice = input("\nPlease select a temperature unit by entering the corresponding number: ")

    temperature_units = {
        "1": "Celsius (°C)",
        "2": "Fahrenheit (°F)",
        "3": "Kelvin (K)"
    }

    if source_unit_choice == "4":
        print("Returning to conversion types menu.")
        return #end actual function and return control to the caller of this function.

    if source_unit_choice in temperature_units:
        source_unit = temperature_units[source_unit_choice]
        print(f"You selected {source_unit}.")
    else:
        print("Invalid choice.")
        return

    #validation of number value
    conversion_value_input = input("\nPlease enter a temperature value to convert: ")
    try:
        conversion_value = float(conversion_value_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    result_display = int(conversion_value) if conversion_value.is_integer() else round(conversion_value, 4)
    print(f"You entered: {result_display} {source_unit}")


    print("\npress enter to continue...")
    input()  # Wait for user to press Enter

    #menu for temperature conversion
    show_temperature_units()

    #choose temperature unit
    second_unit_temperature_choice = input("\nNow, please select the second temperature unit for conversion by entering the corresponding number: ")

    if second_unit_temperature_choice == "4":
        print("Returning to conversion types menu.")
        return

    if second_unit_temperature_choice in temperature_units:
        target_unit = temperature_units[second_unit_temperature_choice]

        if source_unit_choice == second_unit_temperature_choice:
            print("Both selected units are the same. No conversion needed.")
            return

        else:
            value_in_celsius = to_celsius(conversion_value, source_unit)
            result = from_celsius(value_in_celsius, target_unit)

        temperature_result = (
            int(result)
            if result.is_integer()
            else round(result, 4)
        )

        text_result = f"{result_display} {source_unit} is equal to {temperature_result} {target_unit}"

        largura = len(text_result)
        print("\n╔" + "═" * largura + "╗")
        print(f"║{text_result}║")
        print("╚" + "═" * largura + "╝\n")
    else:
        print("Invalid target unit selection.")