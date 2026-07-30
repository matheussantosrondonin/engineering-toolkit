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

#==========================================================



def temperature_converter():
    #menu for temperature conversion
    show_temperature_units()

    #choose temperature unit
    first_unit_temperature_choice = input("\nPlease select a temperature unit by entering the corresponding number: ")

    first_unit_temperature_dict = {
        "1": "Celsius (°C)",
        "2": "Fahrenheit (°F)",
        "3": "Kelvin (K)"
    }

    if first_unit_temperature_choice == "4":
        print("Returning to conversion types menu.")
        return

    if first_unit_temperature_choice in first_unit_temperature_dict:
        selected_unit = first_unit_temperature_dict[first_unit_temperature_choice]
        print(f"You selected {selected_unit}.")
    else:
        print("Invalid choice.")
        return

    conversion_value_input = input("\nPlease enter a temperature value to convert: ")
    try:
        conversion_value = float(conversion_value_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    print(f"You entered: {conversion_value} {selected_unit}")


    print("\npress enter to continue...")
    input()  # Wait for user to press Enter

    #menu for temperature conversion
    show_temperature_units()

    #choose temperature unit
    second_unit_temperature_choice = input("\nNow, please select the second temperature unit for conversion by entering the corresponding number: ")

    second_unit_temperature_dict = {
        "1": "Celsius (°C)",
        "2": "Fahrenheit (°F)",
        "3": "Kelvin (K)"
    }

    if second_unit_temperature_choice == "4":
        print("Returning to conversion types menu.")
        return

    if second_unit_temperature_choice in second_unit_temperature_dict:
        selected_unit_2 = second_unit_temperature_dict[second_unit_temperature_choice]

        if first_unit_temperature_choice == second_unit_temperature_choice:
            print("Both selected units are the same. No conversion needed.")
            return

        else:
            def to_celsius(value, unit):

                if unit == "Celsius (°C)":
                    return value

                elif unit == "Fahrenheit (°F)":
                    return (value - 32) / 1.8

                elif unit == "Kelvin (K)":
                    return value - 273.15

            def from_celsius(value, unit):
                if unit == "Celsius (°C)":
                    return value

                elif unit == "Fahrenheit (°F)":
                    return (value * 1.8) + 32

                elif unit == "Kelvin (K)":
                    return value + 273.15

            value_in_celsius = to_celsius(conversion_value, selected_unit)
            result = from_celsius(value_in_celsius, selected_unit_2)

        text_result = f"{conversion_value} {selected_unit} is equal to {result} {selected_unit_2}"

        largura = len(text_result)
        print("\n╔" + "═" * largura + "╗")
        print(f"║{text_result}║")
        print("╚" + "═" * largura + "╝\n")
    else:
        print("Invalid target unit selection.")