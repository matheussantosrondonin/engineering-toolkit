# ==========================================================
# Project: Engineering Toolkit
# Description: Calcules for conversions.
# Version: 1.0.0
# Author: Matheus Henrique Silva dos Santos
# ==========================================================

# ==========================================================
#pressure_converter.py math
# ==========================================================

def to_pascal(value, unit):
    conversion_factors = {
        "Pa": 1.0,
        "bar": 100000.0,
        "atm": 101325.0,
        "psi": 6894.75729
                }
    return value * conversion_factors[unit]


def from_pascal(value, unit):
    conversion_factors = {
        "Pa": 1.0,
        "bar": 0.00001,
        "atm": 0.00000986923,
        "psi": 0.000145038
                }
    return value * conversion_factors[unit]

# ==========================================================
#temperature_converter.py math
# ==========================================================

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