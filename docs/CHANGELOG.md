# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning**.

---

## [1.0.0] - 2026-08-05

### Added
- Initial Engineering Toolkit project structure.
- Main application entry point (`main.py`).
- Configuration module (`config.py`).
- Utility module (`utils.py`).
- Unit Converter tool.
- Pressure Converter.
- Temperature Converter.
- Length Converter.
- Mass Converter.
- Volume Converter.
- Shared mathematical conversion module (`conversion_math.py`).
- Shared configuration dictionaries for all supported units.
- Reusable result box (`show_result_box()`).
- Menu support for all implemented conversion categories.
- Pressure Calculator module structure.

### Changed
- Refactored all converters to use shared mathematical functions.
- Centralized conversion logic inside `conversion_math.py`.
- Centralized configuration values inside `config.py`.
- Standardized converter workflow across all modules.
- Improved navigation between menus.
- Improved project modularity by separating:
  - User Interface
  - Configuration
  - Mathematical calculations
  - Conversion modules

### Fixed
- Fixed navigation flow between Main Menu and Unit Converter.
- Fixed return behavior from conversion modules.
- Fixed temperature conversion logic using Celsius as an intermediate reference.
- Improved numeric formatting for conversion results.
- Reduced duplicated code across converters.

### Internal
- Improved project architecture.
- Improved maintainability.
- Improved code readability.
- Standardized naming conventions.
- Reduced repeated logic across the project.

---

## [0.2.0] - 2026-07-30

### Added
- Initial Unit Converter module.
- Pressure conversion workflow.
- Pressure unit selection.
- Conversion result formatting.
- Shared configuration lists.

### Changed
- Improved project architecture.
- Replaced repetitive `if/elif` structures with dictionaries.
- Moved shared configuration values to `config.py`.

### Notes
- Pressure conversions use Pascal (Pa) as the reference unit.

---

## [0.1.0] - 2026-07-27

### Added
- Initial project structure.
- Main menu.
- `config.py`
- `utils.py`

### Changed
- Initial modular architecture.

### Fixed
- Initial import organization.
Minha recomendação

Agora que o projeto está ficando grande, eu faria a organização dos arquivos do repositório assim:

Engineering-Toolkit/
│
├── CHANGELOG.md
├── ROADMAP.md
├── DEVLOG.md
├── README.md
├── LICENSE
│
├── main.py
├── config.py
├── utils.py
├── conversion_math.py
│
├── pressure_converter.py
├── temperature_converter.py
├── length_converter.py
├── mass_converter.py
├── volume_converter.py
│
└── pressure_calculator.py