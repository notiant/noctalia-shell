# Translation Period Mismatch Tools

This directory contains tools to identify and analyze inconsistencies in translation files where German translations end with periods (`.`) but their English counterparts don't.

## Files

- `TRANSLATION_PERIOD_MISMATCH_REPORT.md` - Detailed report of all found mismatches
- `check_translation_periods.py` - Python script to check for and report mismatches
- This README

## Quick Start

### View the Report

Simply open `TRANSLATION_PERIOD_MISMATCH_REPORT.md` to see all 15 entries that have period mismatches between German and English translations.

### Run the Script

```bash
# Basic text output
python3 check_translation_periods.py

# JSON output (for programmatic use)
python3 check_translation_periods.py --format=json

# Markdown output
python3 check_translation_periods.py --format=markdown
```

## What Was Found

The script found **15 translation entries** where:
- The German translation (`de.json`) ends with a period (`.`)
- The English translation (`en.json`) does NOT end with a period

**Note:** The original request was to find entries ending with `."` (period + quote), but no such entries exist in either file. The script was adjusted to find entries ending with `.` (period only).

## Examples

### Example 1: `bar.battery.hide-if-not-detected-label`
- **German:** Ausblenden, wenn nicht erkannt.
- **English:** Hide if not detected

### Example 2: `common.check-settings`
- **German:** Überprüfen Sie die Einstellungen für Details.
- **English:** Check Settings for details

## Recommendations

You have three options to address these inconsistencies:

### Option 1: Remove periods from German translations
This would make German match the English style (more common in UI strings).

### Option 2: Add periods to English translations
This would make English match the German style (more formal).

### Option 3: Leave as-is
If this is intentional based on language-specific conventions, no changes are needed.

## Technical Details

The script works by:
1. Loading both `Assets/Translations/de.json` and `Assets/Translations/en.json`
2. Flattening the nested JSON structures into dot-notation keys
3. Comparing each entry to find mismatches in trailing periods
4. Outputting the results in the requested format

## Exit Codes

- `0` - Success, no mismatches found
- `1` - Mismatches found (not necessarily an error)
- `2` - Error occurred (file not found, JSON parse error, etc.)

## Integration

You can integrate this script into your CI/CD pipeline:

```bash
# This will exit with code 1 if mismatches are found
python3 check_translation_periods.py --format=json > mismatches.json
```

## Next Steps

1. Review the `TRANSLATION_PERIOD_MISMATCH_REPORT.md` file
2. Decide on your preferred style (with or without periods)
3. Update the appropriate translation file(s)
4. Run the script again to verify fixes
