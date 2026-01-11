# Translation Period Mismatch Report

**Date:** 2026-01-11  
**Files Analyzed:** `Assets/Translations/de.json` and `Assets/Translations/en.json`

## Summary

- **Total mismatches found:** 15
- **Pattern:** Entries ending with `.` in `de.json` but not in `en.json`
- **Note:** No entries were found ending with `."` in either file

## Detailed Findings

### 1. `bar.battery.hide-if-not-detected-label`

**German (de.json):** Ausblenden, wenn nicht erkannt.

**English (en.json):** Hide if not detected

---

### 2. `bar.workspace.grouped-border-opacity-description`

**German (de.json):** Lege die Deckkraft für Workspace-Container-Rahmen fest.

**English (en.json):** Set the opacity level for workspace container borders

---

### 3. `common.check-settings`

**German (de.json):** Überprüfen Sie die Einstellungen für Details.

**English (en.json):** Check Settings for details

---

### 4. `launcher.providers.calculator-press-enter-to-copy`

**German (de.json):** Drücken Sie die Eingabetaste, um das Ergebnis zu kopieren.

**English (en.json):** Press Enter to copy result

---

### 5. `launcher.providers.emoji-no-recent`

**German (de.json):** Noch keine kürzlich verwendeten Emojis.

**English (en.json):** No recent emojis yet

---

### 6. `panels.about.system-install-hint`

**German (de.json):** Installiere fastfetch, um Systeminformationen anzuzeigen.

**English (en.json):** Install fastfetch to view system information

---

### 7. `panels.audio.panel-applications-empty`

**German (de.json):** Derzeit geben keine Anwendungen Audio wieder.

**English (en.json):** No applications are currently playing audio

---

### 8. `panels.plugins.collision-already-installed`

**German (de.json):** Dieses Plugin ist bereits installiert.

**English (en.json):** This plugin is already installed

---

### 9. `panels.plugins.collision-custom-version-exists`

**German (de.json):** Eine benutzerdefinierte Version von "{source}" ist bereits installiert.

**English (en.json):** A custom version from "{source}" is already installed

---

### 10. `panels.plugins.collision-official-version-exists`

**German (de.json):** Die offizielle Version dieses Plugins ist bereits installiert.

**English (en.json):** The official version of this plugin is already installed

---

### 11. `panels.plugins.install-incompatible`

**German (de.json):** {plugin} benötigt Noctalia v{version} oder höher.

**English (en.json):** {plugin} requires Noctalia v{version} or higher

---

### 12. `panels.plugins.uninstall-success`

**German (de.json):** {plugin} wurde erfolgreich deinstalliert.

**English (en.json):** Successfully uninstalled {plugin}

---

### 13. `wifi.panel.disconnecting`

**German (de.json):** Verbindung wird getrennt...

**English (en.json):** Disconnecting…

---

### 14. `wifi.panel.enter-password`

**German (de.json):** Passwort eingeben...

**English (en.json):** Enter Wi‑Fi password

---

### 15. `wifi.panel.forgetting`

**German (de.json):** Wird vergessen...

**English (en.json):** Forgetting…

---

## Recommendations

The German translations end with a period (`.`) while the English equivalents do not. This appears to be a stylistic difference in the translations.

### Options:

1. **Remove periods from German translations** to match English style
2. **Add periods to English translations** to match German style
3. **Leave as-is** if this is intentional based on language conventions

### Notes:

- German language conventions often require periods at the end of complete sentences, even in UI strings
- English UI strings typically omit periods for brevity
- The choice depends on your project's localization guidelines

## How to Use This Report

To fix these inconsistencies, you can:

1. Review each entry and decide whether to add/remove the period
2. Use the accompanying Python script to generate an updated version
3. Update either `de.json` or `en.json` to maintain consistency

## Script

A Python script is included (`check_translation_periods.py`) that can:
- Find all mismatches
- Generate this report
- Optionally fix the inconsistencies automatically
