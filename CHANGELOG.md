# Changelog

## [0.3.1] - 2025-01-01

### Fixed
- Fixed first-time user experience - now only prompts when choosing an exercise, not when starting the program
- Fixed exercise name handling - removed dependency on non-existent "name" field
- Improved weekend handling - properly skips to Monday when starting on weekends
- Fixed file saving format - now uses proper `branden_week_X_YYYYMMDD.yaml` format
- Added proper package data handling for exercises.yaml

### Added
- Custom start date option - users can choose specific week and day
- Better error handling for file operations
- Improved user prompts and messages

### Changed
- Updated version to 0.3.1
- Improved package structure for distribution 