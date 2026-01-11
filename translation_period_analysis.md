# Translation Period Consistency Analysis Report

## Summary

**Request**: Find entries that end with `.` in `en.json` but don't in `de.json`

**Result**: **0 entries found** ✓

All entries that end with a period in `en.json` also end with a period in `de.json`.

## Statistics

- **Total entries in each file**: 1,478
- **Entries ending with `.` in en.json**: 474
- **Entries ending with `.` in de.json**: 488
- **EN has period, DE doesn't**: 0 ✓
- **DE has period, EN doesn't**: 14

## Detailed Findings

### Requested Search: EN has `.` but DE doesn't
**Count: 0** - No mismatches found in this direction.

This indicates excellent consistency in the translation work, where all English entries with periods have been properly translated to German with matching punctuation.

---

### Reverse Issue Discovered: DE has `.` but EN doesn't
**Count: 14** - These entries have periods in German but not in English:

#### 1. `bar.battery.hide-if-not-detected-label`
- **EN**: Hide if not detected
- **DE**: Ausblenden, wenn nicht erkannt.

#### 2. `bar.workspace.grouped-border-opacity-description`
- **EN**: Set the opacity level for workspace container borders
- **DE**: Lege die Deckkraft für Workspace-Container-Rahmen fest.

#### 3. `common.check-settings`
- **EN**: Check settings for details
- **DE**: Überprüfen Sie die Einstellungen für Details.

#### 4. `launcher.providers.calculator-press-enter-to-copy`
- **EN**: Press Enter to copy result
- **DE**: Drücken Sie die Eingabetaste, um das Ergebnis zu kopieren.

#### 5. `launcher.providers.emoji-no-recent`
- **EN**: No recent emojis yet
- **DE**: Noch keine kürzlich verwendeten Emojis.

#### 6. `panels.audio.panel-applications-empty`
- **EN**: No applications are currently playing audio
- **DE**: Derzeit geben keine Anwendungen Audio wieder.

#### 7. `panels.plugins.collision-already-installed`
- **EN**: This plugin is already installed
- **DE**: Dieses Plugin ist bereits installiert.

#### 8. `panels.plugins.collision-custom-version-exists`
- **EN**: A custom version from "{source}" is already installed
- **DE**: Eine benutzerdefinierte Version von "{source}" ist bereits installiert.

#### 9. `panels.plugins.collision-official-version-exists`
- **EN**: The official version of this plugin is already installed
- **DE**: Die offizielle Version dieses Plugins ist bereits installiert.

#### 10. `panels.plugins.install-incompatible`
- **EN**: {plugin} requires Noctalia v{version} or higher
- **DE**: {plugin} benötigt Noctalia v{version} oder höher.

#### 11. `panels.plugins.uninstall-success`
- **EN**: Successfully uninstalled {plugin}
- **DE**: {plugin} wurde erfolgreich deinstalliert.

#### 12. `wifi.panel.disconnecting`
- **EN**: Disconnecting…
- **DE**: Verbindung wird getrennt...

#### 13. `wifi.panel.enter-password`
- **EN**: Enter Wi‑Fi password
- **DE**: Passwort eingeben...

#### 14. `wifi.panel.forgetting`
- **EN**: Forgetting…
- **DE**: Wird vergessen...

## Recommendations

1. **For the requested search**: No action needed. All EN entries with periods are consistently translated.

2. **For the reverse mismatches**: Consider whether these 14 German entries should have their periods removed to match English, or if English should add periods to match German style.

## Analysis Method

The analysis was performed using a Python script that:
1. Loaded both JSON translation files
2. Flattened nested structures to dot-notation keys
3. Compared each entry's ending punctuation
4. Identified mismatches in both directions

Files analyzed:
- `Assets/Translations/en.json`
- `Assets/Translations/de.json`
