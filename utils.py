# ==========================================================
# Project: Engineering Toolkit
# Description: Functions for developed during Project Atlas.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================


#==========================================================
# importing the necessary modules
#==========================================================

from config import separator, tool_name, version, author_name, app_converter,list_of_tools, list_of_conversion_types, list_of_pressure_units, list_of_temperature_units

#==========================================================
# Function to display the header information
#========================================================== 

def show_header():
    print(separator)
    print(f"Welcome to the {tool_name}!")
    print(f"Version: {version}")
    print(f"Author: {author_name}")
    print(separator)

#========================================================== 
# Function to display the header Unit Converter
#========================================================== 

def show_tool_menu():
    print(separator)
    print("Available Tools:")
    for tool in list_of_tools:
        print(tool)
    print(separator)

def show_conversion_types():
    print(separator)
    print(app_converter)
    print(separator)
    print("Available Conversion Types:")
    for conversion_type in list_of_conversion_types:
        print(conversion_type)
    print(separator)

def show_pressure_units():
    print(separator)
    print("Available Pressure Units:")
    for pressure_unit in list_of_pressure_units:
        print(pressure_unit)
    print(separator)

def show_temperature_units():
    print(separator)
    print("Available Temperature Units:")
    for temperature_unit in list_of_temperature_units:
        print(temperature_unit)
    print(separator)