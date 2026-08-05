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


# ==========================================================
#length_converter.py math
# ==========================================================

def to_meter(value, unit):
    conversion_factors = {
        "Meter (m)": 1.0,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Kilometer (km)": 1000.0
    }
    return value * conversion_factors[unit]

def from_meter(value, unit):
    conversion_factors = {
        "Meter (m)": 1.0,
        "Centimeter (cm)": 100.0,
        "Millimeter (mm)": 1000.0,
        "Kilometer (km)": 0.001
    }
    return value * conversion_factors[unit]

# ==========================================================
#mass_converter.py math
# ==========================================================

def to_grams(value, unit):
    conversion_factors = {
        "Kilogram (kg)": 1000.0,
        "Gram (g)": 1.0,
        "Milligram (mg)": 0.001,
        "Pound (lb)": 453.59237
    }
    return value * conversion_factors[unit]

def from_grams(value, unit):
    conversion_factors = {
        "Kilogram (kg)": 0.001,
        "Gram (g)": 1.0,
        "Milligram (mg)": 1000.0,
        "Pound (lb)": 0.00220462
    }
    return value * conversion_factors[unit]

# ==========================================================
#volume_converter.py math
# ==========================================================

def to_liters(value, unit):
    conversion_factors = {
        "Liter (L)": 1.0,
        "Milliliter (mL)": 0.001,
        "Cubic Meter (m³)": 1000.0,
        "Gallon (gal)": 3.78541
    }
    return value * conversion_factors[unit]

def from_liters(value, unit):
    conversion_factors = {
        "Liter (L)": 1.0,
        "Milliliter (mL)": 1000.0,
        "Cubic Meter (m³)": 0.001,
        "Gallon (gal)": 0.264172
    }
    return value * conversion_factors[unit]