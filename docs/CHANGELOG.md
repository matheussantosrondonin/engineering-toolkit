1.0.0

Initial release

Added

- Config module

- Utils module

- Main menu

Changed

- Project architecture

Fixed

- Imports


# Changelog

## Version 0.2.0

### Added

- Initial Unit Converter module.
- Pressure conversion workflow.
- Pressure unit selection.
- Conversion result formatting.
- Shared configuration lists.

### Changed

- Improved project architecture.
- Moved shared values to `config.py`.
- Reduced multiple `if/elif` statements using dictionaries.

### Notes

Pressure conversions are now performed using Pascal (Pa) as the reference unit.


Adicione:

```md
## [Unreleased] - 2026-07-27

### Added

- Added `pressure_converter.py` as a dedicated pressure conversion module.
- Added `temperature_converter.py` as the initial temperature conversion module.
- Added `show_conversion_types()` to `utils.py`.

### Changed

- Improved navigation between the main menu and Unit Converter.
- Added continuous navigation loops to `main.py` and `unit_converter.py`.
- Implemented return from Unit Converter to the main menu.
- Implemented return from Pressure Converter to the Unit Converter.
- Centralized conversion-type menu display in `utils.py`.
- Improved separation of responsibilities between modules.

### Fixed

- Fixed menu navigation behavior after completing a conversion.
- Fixed the previous behavior where the Unit Converter could not properly return control to the main menu.