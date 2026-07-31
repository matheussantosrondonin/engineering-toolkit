# ==========================================================
# Project: Engineering Toolkit
# Description: Pressure conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

#==========================================================
# importing the necessary modules
#==========================================================
from utils import show_pressure_units
from conversion_math import (to_pascal, from_pascal)
#==========================================================



def pressure_converter():
        #menu for pressure conversion
        show_pressure_units()
            
        #choose pressure unit
        source_unit_choice = input("\nPlease select a pressure unit by entering the corresponding number: ")

        pressure_units = {
            "1": "Pa",
            "2": "bar",
            "3": "atm",
            "4": "psi"
        }

        if source_unit_choice == "5":
            print("Returning to conversion types menu.")
            return  #end actual function and return control to the caller of this function.
    
        if source_unit_choice in pressure_units:
            source_unit = pressure_units[source_unit_choice]
            print(f"You selected {source_unit}.")
        else:
            print("Invalid choice.")
            return
    
        #validation of number value
        conversion_value_input = input("\nPlease enter a value: ")
        try:
            conversion_value = float(conversion_value_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
    
        # Formata o número inserido para exibição limpa
        result_display = int(conversion_value) if conversion_value.is_integer() else round(conversion_value, 2)
        print(f"You entered: {result_display} {source_unit}")

        print("\npress enter to continue...")
        input()  # Wait for user to press Enter
    
        #menu for pressure conversion
        show_pressure_units()

        #choose pressure unit
        target_unit_choice = input("\nNow, please select the second pressure unit for conversion:\n")
    
        if target_unit_choice == "5":
            print("Returning to conversion types menu.")
            return  #encerra a função atual e devolve o controle para quem chamou essa função.
            
        if target_unit_choice in pressure_units:
            target_unit = pressure_units[target_unit_choice]
    
            # Formata o resultado final (int ou float com até 4 casas)
            value_in_pascal = to_pascal(conversion_value, source_unit)
            result = from_pascal(value_in_pascal, target_unit)
                
            # Monta a string do resultado
            pressure_result = int(result)if result.is_integer()else round(result, 4)
            
            text_result = f" Conversion result: {result_display} {source_unit} = {pressure_result} {target_unit} "

            #Desenha a caixa de resposta no terminal do VS Code
            largura = len(text_result)
            print("\n╔" + "═" * largura + "╗")
            print(f"║{text_result}║")
            print("╚" + "═" * largura + "╝\n")
        else:
            print("Invalid target unit selection.")