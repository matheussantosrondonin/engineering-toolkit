# ==========================================================
# Project: Engineering Toolkit
# Description: Functions for developed during Project Atlas.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================


#==========================================================
# importing the necessary modules
#==========================================================

from config import separator, tool_name, version, author_name, app_converter

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

def show_converter_header():
    print(separator)
    print(app_converter)
    print(separator)