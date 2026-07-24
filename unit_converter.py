# ==========================================================
# Project: Engineering Toolkit
# Description: Unit conversion functions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

#==========================================================
# importing the necessary modules
#==========================================================

from py_compile import main

from config import list_of_conversion_types, list_of_pressure_units
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
    if menu_choice == "1":
        print("\nAvailable pressure units:\n")
        for pressure_unit in list_of_pressure_units:
            print(f"  {pressure_unit}")
        
        # 2. Escolha da PRIMEIRA unidade (Origem)
        unit_choice = input("\nPlease select a pressure unit by entering the corresponding number: ")

        if unit_choice == "1":
            print("You selected Pascal (Pa).")
            unit = "Pa"
        elif unit_choice == "2":
            print("You selected Bar (bar).")
            unit = "bar"
        elif unit_choice == "3":
            print("You selected Atmosphere (atm).")
            unit = "atm"
        elif unit_choice == "4":
            print("You selected Pounds per Square Inch (psi).")
            unit = "psi"
        elif unit_choice == "5":
            print("Returning to conversion types menu.")
            main()  # Retorna ao menu principal
        else:
            print("Invalid choice.")
            return

        # 3. Leitura e validação do valor numérico
        value_input = input("\nPlease digita a value: ")
        num_1 = float(value_input)

        # Formata o número inserido para exibição limpa
        num_1_display = int(num_1) if num_1.is_integer() else round(num_1, 2)
        print(f"You entered: {num_1_display} {unit}")

        # 4. Escolha da SEGUNDA unidade (Destino)
        print("\nAvailable pressure units:\n")
        for pressure_unit in list_of_pressure_units:
            print(f"  {pressure_unit}")
        target_choice = input("\nNow, please select the second pressure unit for conversion:\n")

        # Mapeamento da escolha numérica para a string da unidade
        unidades_mapeadas = {"1": "Pa", "2": "bar", "3": "atm", "4": "psi"}

        if target_choice == "5":
            print("Returning to conversion types menu.")
            main()  # Retorna ao menu principal
        
        if target_choice in unidades_mapeadas:
            target_unit = unidades_mapeadas[target_choice]
            
            # Se forem iguais, não há cálculo
            if unit == target_unit:
                result = num_1
            else:
                # Fatores universais baseados em 1 Pascal (Pa)
                fatores_para_pa = {"Pa": 1.0, "bar": 100000.0, "atm": 101325.0, "psi": 6894.75729}
                
                # Cálculo inteligente: converte para Pa e depois para o destino
                valor_em_pa = num_1 * fatores_para_pa[unit]
                result = valor_em_pa / fatores_para_pa[target_unit]

            # Formata o resultado final (int ou float com até 4 casas)
            result_display = int(result) if result.is_integer() else round(result, 4)
            
            # Monta a string do resultado
            texto_resultado = f" Conversion result: {num_1_display} {unit} = {result_display} {target_unit} "
            
            # Desenha a caixa de resposta no terminal do VS Code
            largura = len(texto_resultado)
            print("\n╔" + "═" * largura + "╗")
            print(f"║{texto_resultado}║")
            print("╚" + "═" * largura + "╝\n")
        else:
            print("Invalid target unit selection.")

        
        
        

    
    # You can add functions for converting pressure, temperature, length, mass, and volume

# ==========================================================




