Version 1.0.0

Initial project structure

Added:

✔ main.py

✔ config.py

✔ utils.py

✔ pressure_calculator.py

✔ unit_converter.py

Implemented:

✔ show_header()

Improved:

✔ modular architecture

Next version:

⬜ reusable menu

⬜ pressure conversion

⬜ temperature conversion

# Development Log

## Day 02

### Objective

Start implementing the first functional module.

### Progress

Implemented the Unit Converter module.

The pressure conversion workflow now performs the following steps:

1. User selects Pressure.
2. Selects source unit.
3. Enters the value.
4. Selects destination unit.
5. Receives the converted value.

### Improvements

- Centralized configuration values.
- Created reusable converter header.
- Introduced dictionaries to replace repetitive conditional structures.

### Next Steps

- Return to Main Menu.
- Temperature conversions.
- Input validation.



# Development Log

## Week 2 — Day 01
**Date:** 2026-07-27

### Focus

Today's development focused on improving the navigation architecture of the Engineering Toolkit.

The main objective was to make the application capable of moving between the main menu, the Unit Converter, and its conversion modules without requiring each module to directly control the previous menu.

---

### What Was Implemented

#### 1. Main Menu Navigation

The main menu was reorganized using a continuous `while True` loop.

The application now:

1. Displays the main menu.
2. Receives the user's choice.
3. Validates the option.
4. Executes the selected tool.
5. Returns to the main menu after the tool finishes.
6. Continues until the user selects `3 - Exit`.

The main navigation is now controlled by `main.py`.

This established the idea that `main.py` is responsible for controlling the application's highest-level navigation.

---

### 2. Unit Converter Navigation

The `unit_converter.py` module was changed to use its own navigation loop.

The Unit Converter now controls its own conversion-type menu:

Unit Converter
│
├── 1 - Pressure
├── 2 - Temperature
├── 3 - Length
├── 4 - Mass
├── 5 - Volume
└── 6 - Return to Main Menu

The module remains active while the user wants to perform conversions.

Selecting:

6 - Return to Main Menu

causes unit_converter() to execute:

return

This ends the current function and returns control to main.py.

---

### 3. Pressure Converter Module

The pressure conversion logic was separated from unit_converter.py into:

pressure_converter.py

This was an important structural improvement.

Instead of having all conversion logic inside the Unit Converter, the responsibility is now divided:

main.py
    ↓
unit_converter.py
    ↓
pressure_converter.py

Each module has a more specific responsibility.

The pressure_converter() function returns to unit_converter() when the user selects:

5 - Return to Conversion Types

The Unit Converter then continues controlling its own menu.

### 4. Temperature Converter Module

A new module was created:

temperature_converter.py

At the moment, it contains a placeholder implementation indicating that temperature conversion is under development.

This establishes the structure that will later be used for additional conversion types.

### 5. Utility Functions

The utils.py module was reorganized.

A new function was created:

show_conversion_types()

This function is responsible for displaying the Unit Converter menu.

The responsibility is therefore separated from unit_converter.py.

The current structure is becoming:

config.py
    ↓
utils.py
    ↓
unit_converter.py
    ↓
pressure_converter.py
temperature_converter.py

This reduces repeated menu-printing code and makes future changes easier.

### 6. Navigation and Function Responsibility

One of the most important lessons from today's development was understanding how functions return control to the function that called them.

For example:

if option_tool == "1":
    unit_converter()

When unit_converter() calls:

pressure_converter()

the flow becomes:

main.py
   ↓
unit_converter()
   ↓
pressure_converter()

When pressure_converter() executes:

return

it does not return directly to main.py.

It returns to the function that called it:

pressure_converter()
   ↑
unit_converter()

Then, when unit_converter() eventually executes:

return

control goes back to:

main.py

This helped clarify the difference between:

ending a function;
returning control to its caller;
continuing a loop;
returning to a higher-level menu.
### 7. while True and Navigation

The project initially attempted to control navigation using several independent while conditions.

This created confusion because the program needed to know which component was responsible for each level of navigation.

The current structure uses:

while True:

for the main application and for the Unit Converter.

The loop is terminated explicitly when the corresponding exit option is selected.

For example:

if option_tool == "3":
    break

and:

if menu_choice == "6":
    return

This made the navigation considerably clearer.

### 8. Important Learning

Today's main lesson was that navigation should follow the responsibility hierarchy of the application.

The current architecture can be represented as:

Engineering Toolkit
│
└── main.py
      │
      ├── Unit Converter
      │     │
      │     ├── Pressure Converter
      │     │
      │     ├── Temperature Converter
      │     │
      │     ├── Length Converter
      │     │
      │     └── Volume Converter
      │
      └── Pressure Calculator

Each level is responsible for its own menu and delegates specialized work to the appropriate module.

This is helping move the project away from a single large script and toward a modular architecture.

Current Status

The navigation between the main menu and Unit Converter is now functional.

Current implemented structure:

Main menu
Unit Converter
Pressure Converter
Temperature Converter placeholder
Return to Conversion Types
Return to Main Menu
Exit application
Input validation for main menus
Shared menu display functions in utils.py
Next Steps

The next development steps are:

Improve input validation inside the conversion modules.
Complete temperature conversion.
Review the pressure conversion logic.
Implement additional conversion types.
Reduce duplicated code where appropriate.
Reassess the navigation architecture as the number of tools increases.