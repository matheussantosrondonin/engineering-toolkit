# Development Log

This document records the daily development progress of the Engineering Toolkit, including implementation details, architectural decisions, lessons learned, and future plans.

---

# Week 1 — Day 1
**Date:** 2026-07-26

## Objective

Initialize the Engineering Toolkit project structure.

## Completed

- Created the project architecture.
- Added `main.py`.
- Added `config.py`.
- Added `utils.py`.
- Added `pressure_calculator.py`.
- Added `unit_converter.py`.
- Implemented the application header.
- Created the initial menu system.

## Lessons Learned

- Importance of separating configuration from business logic.
- Benefits of creating reusable utility functions early.

## Next Steps

- Improve menu navigation.
- Implement the first conversion module.
- Add pressure conversion.

---

# Week 1 — Day 2
**Date:** 2026-07-27

## Objective

Implement the first functional conversion module.

## Completed

- Created the Pressure Converter.
- Implemented pressure unit selection.
- Added numeric input validation.
- Added pressure conversion calculations.
- Displayed formatted conversion results.

## Improvements

- Centralized configuration values.
- Replaced repetitive conditionals with dictionaries.
- Improved code readability.

## Lessons Learned

Using dictionaries instead of multiple `if/elif` statements makes the code cleaner and easier to maintain.

## Next Steps

- Implement temperature conversion.
- Improve menu navigation.

---

# Week 2 — Day 1
**Date:** 2026-07-30

## Objective

Improve application navigation and modular architecture.

## Completed

### Main Menu

- Reworked the application navigation using `while True`.
- Centralized top-level navigation in `main.py`.

### Unit Converter

- Added an independent navigation loop.
- Implemented "Return to Main Menu".

### Pressure Converter

- Moved pressure conversion into its own module.
- Improved module responsibility separation.

### Temperature Converter

- Created the initial module structure.

### Utilities

- Added reusable menu display functions.

## Architecture

Current hierarchy:

```
main.py
│
├── unit_converter.py
│   ├── pressure_converter.py
│   ├── temperature_converter.py
│   ├── length_converter.py
│   └── ...
│
└── pressure_calculator.py
```

## Lessons Learned

A function always returns to the function that called it.

Understanding this simplified the application's navigation architecture considerably.

## Next Steps

- Complete Temperature Converter.
- Improve validation.
- Continue modularization.

---

# Week 2 — Day 2
**Date:** 2026-08-01

## Objective

Implement the Temperature Converter.

## Completed

- Created the temperature conversion workflow.
- Added source and target unit selection.
- Added numeric validation.
- Implemented Celsius intermediary conversion model.

## Technical Decision

Unlike pressure conversion, temperature cannot be converted using a single multiplication factor.

The adopted workflow is:

```
Original Unit
      │
      ▼
  Celsius
      │
      ▼
Target Unit
```

This approach simplifies future maintenance and expansion.

## Lessons Learned

- Function parameters
- Return values
- Data flow
- Intermediate conversion architecture

## Next Steps

- Refactor repeated code.
- Improve formatting.
- Add additional converters.

---

# Week 3 — Day 1
**Date:** 2026-08-05

## Objective

Expand the Unit Converter and improve the project's architecture.

## Completed

### New Converters

- Added Length Converter.
- Added Mass Converter.
- Added Volume Converter.

### Shared Conversion Logic

Created `conversion_math.py` containing:

- Pressure conversion functions
- Temperature conversion functions
- Length conversion functions
- Mass conversion functions
- Volume conversion functions

### Configuration

Moved all unit dictionaries into `config.py`.

Added:

- Pressure units
- Temperature units
- Length units
- Mass units
- Volume units

### Utilities

Improved `utils.py` by adding reusable functions:

- `show_result_box()`
- Unit display menus
- Shared menu utilities

### Refactoring

Standardized every converter to follow the same workflow:

1. Select source unit
2. Enter value
3. Select target unit
4. Perform conversion
5. Display formatted result

This significantly reduced duplicated code and improved maintainability.

## Current Architecture

```
main.py
│
├── config.py
├── utils.py
├── conversion_math.py
│
├── unit_converter.py
│
├── pressure_converter.py
├── temperature_converter.py
├── length_converter.py
├── mass_converter.py
├── volume_converter.py
│
└── pressure_calculator.py
```

## Lessons Learned

One of the biggest improvements was separating responsibilities into three distinct layers:

- Configuration (`config.py`)
- Mathematical logic (`conversion_math.py`)
- User interface (`*_converter.py`)

This architecture makes adding future converters significantly easier.

## Next Steps

- Improve input validation.
- Eliminate remaining duplicated code.
- Begin development of the Pressure Calculator.
- Implement additional engineering converters.