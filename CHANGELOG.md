# Changelog

## [0.4.0] - 2025-01-06

### Fixed
- **Smart weekday calculation** - Now only counts Monday-Friday (weekdays 0-4) instead of all calendar days
- **Consistent file naming** - Updated to use `exercisename_YYMMDD.yaml` format (e.g., `210431`) throughout
- **Submit logic consistency** - All prompts now use "type submit" (no quotes) with exact matching
- **Weekend reflection improvements** - Handles partial weeks properly, compiles even if only 1 day exists
- **Session timing** - Proper start/end time tracking and duration calculation
- **Streak calculation** - Real streak calculation based on actual submission patterns
- **Analytics improvements** - Added month selection and day-specific viewing
- **Error handling** - Better error messages and graceful failures throughout

### Added
- **Month selection in analytics** - Users can view different months
- **Day-specific submission viewing** - View submissions for specific dates
- **Proper session timing** - Track start/end times and calculate duration
- **Real streak calculation** - Based on 6+ sessions per week
- **Better weekend handling** - Dynamic week/day display instead of hardcoded values

### Changed
- **File naming format** - Consistent `exercisename_210431.yaml` format
- **Week calculation** - Uses 6 weekdays per week instead of 7 calendar days
- **Submit prompts** - Consistent "type submit" without quotes
- **Progress tracking** - Improved with proper `last_completed` field
- **Removed unused code** - Cleaned up `stems_per_day` and `is_new_user` fields

### Technical
- Removed unused `date` import
- Improved error handling for file operations
- Better session data management
- Enhanced analytics with real data

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