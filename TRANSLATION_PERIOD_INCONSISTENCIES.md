# Translation Period Inconsistencies Report

This report lists all entries in translation files that have period inconsistencies with `en.json`.

**Note:** For `zh-CN.json` and `ja.json`, the analysis checks for both `.` (regular period) and `。` (full-width period).

## Summary

| File | Inconsistencies |
|------|-----------------|
| de.json | 1 |
| es.json | 8 |
| fr.json | 6 |
| hu.json | 6 |
| ja.json | 27 |
| ku.json | 5 |
| nl.json | 3 |
| pl.json | 4 |
| pt.json | 13 |
| ru.json | 7 |
| tr.json | 11 |
| uk-UA.json | 4 |
| zh-CN.json | 7 |
| **TOTAL** | **102** |

## Categories of Issues

### 1. EN has period, translation does NOT
This is the most common type - where English text ends with `.` but the translation doesn't.

### 2. Translation has period, EN does NOT  
Where the translation ends with `.` but the English text doesn't.

---

## Detailed Findings by File

### de.json (1 inconsistency)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `panels.plugins.install-error` | EN has period, translation does not | `Failed to install: {error}.` | `Installation fehlgeschlagen: {error}` |

---

### es.json (8 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Utilice fuente monoespaciada para un ancho de carácter consistente.\n` |
| `launcher.providers.emoji-no-recent` | Translation has period, EN does not | `No recent emojis yet` | `Aún no hay emojis recientes.` |
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `Tiempo en segundos para que el título se desplace del inicio al final` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `Activar desplazamiento continuo para títulos de medios largos` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Mostrar u ocultar el dock por completo` |
| `panels.plugins.available-no-plugins-label` | Translation has period, EN does not | `No plugins available` | `No hay plugins disponibles.` |
| `panels.plugins.installed-no-plugins-label` | Translation has period, EN does not | `No plugins installed` | `No hay plugins instalados.` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Carga prom.` |

---

### fr.json (6 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `Temps en secondes pour que le titre défile du début à la fin` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `Activer le défilement continu pour les titres multimédias longs` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Afficher ou masquer complètement le dock` |
| `panels.plugins.update-incompatible` | Translation has period, EN does not | `Requires Noctalia v{version} or higher` | `Nécessite Noctalia v{version} ou une version ultérieure.` |
| `panels.plugins.update-success` | Translation has period, EN does not | `Updated {plugin} to v{version}` | `Mise à jour du plugin {plugin} vers la version {version}.` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Charge moy.` |

---

### hu.json (6 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Használj monospace betűtípust az egységes karakter-szélességhez.\n` |
| `common.none` | Translation has period, EN does not | `None` | `Nincs.` |
| `panels.notifications.sounds-excluded-apps-description` | EN has period, translation does not | `Skip playing the configured notification sound for specific applications that have their own built-in sounds.` | `Kizárt alkalmazások` |
| `panels.notifications.sounds-excluded-apps-label` | Translation has period, EN does not | `Excluded applications` | `A beállított értesítési hang lejátszásának kihagyása bizonyos alkalmazásoknál, amelyek saját beépített hangokkal rendelkeznek.` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Terh. átl.` |
| `wifi.panel.searching` | EN has period, translation does not | `Searching for networks...` | `Hálózatok keresése…` |

---

### ja.json (27 inconsistencies)

**Note:** Japanese uses `。` (full-width period) which is checked alongside `.`

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `actions.lower-to-bottom` | Translation has period, EN does not | `Lower to bottom` | `一番下まで下げてください。` |
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `タイプライター体で翻訳します。\n\n` |
| `changelog.panel.buttons-feedback` | Translation has period, EN does not | `Give feedback` | `フィードバックをお願いします。` |
| `panels.audio.volumes-input-volume-description` | EN has period, translation does not | `Microphone input volume level.` | `マイクの音量レベル` |
| `panels.color-scheme.templates-compositors-description` | EN has period, translation does not | `Compositor theming.` | `コンポジタのテーマ設定` |
| `panels.color-scheme.templates-compositors-mango-description` | Translation has period, EN does not | `Write {filepath} — requires Mango` | `{filepath} を書き込みます。Mango が必要です。` |
| `panels.color-scheme.templates-compositors-niri-description` | Translation has period, EN does not | `Write {filepath} — requires Niri v25.11+` | `{filepath} を書き込みます。Niri v25.11+ が必要です。` |
| `panels.color-scheme.templates-misc-user-templates-description` | Translation has period, EN does not | `Only enable if you know what you are doing — refer to our online documentation` | `操作方法を理解している場合のみ有効にしてください。オンラインドキュメントを参照してください。` |
| `panels.color-scheme.templates-programs-description` | EN has period, translation does not | `Application-specific theming.` | `アプリケーションごとのテーマ設定` |
| `panels.color-scheme.templates-programs-discord-description` | Translation has period, EN does not | `Write {filepath} for {client} — the theme needs to be activated manually` | `{client} 用に {filepath} を書き込みます。テーマを手動で有効化する必要があります。` |
| `panels.color-scheme.templates-programs-pywalfox-description` | Translation has period, EN does not | `Write {filepath} and run 'pywalfox update'` | `{filepath} を書き込みます、'pywalfox update' を実行します。` |
| `panels.color-scheme.templates-programs-spicetify-description` | Translation has period, EN does not | `Write {filepath} — Comfy theme needs to be installed and activated manually` | `{filepath} を書き込みます。Comfy テーマを手動でインストールして有効化する必要があります。` |
| `panels.color-scheme.templates-programs-walker-description` | Translation has period, EN does not | `Write {filepath} and set theme to noctalia` | `{filepath} を書き込みます、テーマを noctalia に設定します。` |
| `panels.color-scheme.templates-programs-yazi-description` | Translation has period, EN does not | `Write {filepath} — flavor needs to be activated manually` | `{filepath} を書き込みます。フレーバーは手動で有効化する必要があります。` |
| `panels.color-scheme.templates-programs-zed-description` | Translation has period, EN does not | `Write {filepath} and reload` | `{filepath} を書き込みます、リロードします。` |
| `panels.color-scheme.templates-programs-zen-browser-description` | Translation has period, EN does not | `Write {filepath} — copy into your Zen profile's chrome/userChrome.css` | `{filepath} を書き込みます 。Zen プロファイルの chrome/userChrome.css にコピーしてください。` |
| `panels.color-scheme.templates-terminal-description` | EN has period, translation does not | `Terminal emulator theming.` | `ターミナルエミュレータのテーマ設定` |
| `panels.color-scheme.templates-ui-description` | EN has period, translation does not | `Desktop environment and UI toolkit theming.` | `デスクトップ環境と UI ツールキットのテーマ設定` |
| `panels.color-scheme.templates-ui-qt-description` | Translation has period, EN does not | `Write {filepath}` | `{filepath} を書き込みます。` |
| `panels.plugins.update-incompatible` | Translation has period, EN does not | `Requires Noctalia v{version} or higher` | `Noctalia v{version} 以降が必要です。` |
| `panels.plugins.update-success` | Translation has period, EN does not | `Updated {plugin} to v{version}` | `{plugin} を v{version} にアップデートしました。` |
| `setup.wallpaper.choose-dir` | Translation has period, EN does not | `Choose a directory containing your wallpaper images` | `壁紙画像が含まれているフォルダを選択します。` |
| `setup.wallpaper.dir-description` | Translation has period, EN does not | `Choose the folder containing your wallpapers` | `壁紙画像が含まれているフォルダを選択します。` |
| `setup.welcome-note` | Translation has period, EN does not | `Just a few basics to get you started — full options are in the settings` | `まずは基本設定から始めましょう。詳細なオプションは「設定」にあります。` |
| `wallpaper.panel.apikey-placeholder` | Translation has period, EN does not | `Enter your Wallhaven API Key` | `Wallhaven APIキーを入力してください。` |
| `widgets.color-picker.palette-theme-colors` | EN has period, translation does not | `Quick access to your theme's color palette.` | `テーマのカラーパレット` |
| `widgets.file-picker-title` | Translation has period, EN does not | `Select a file` | `ファイルを選択してください。` |

---

### ku.json (5 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.control-center.use-distro-logo-label` | Translation has period, EN does not | `Use distro logo instead of icon` | `Li şûna îkonê logoya belavkirina bi kar bîne.` |
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Bi kar tîne fonta monospace ji bo firehiya karakterê ya domdar.\n` |
| `panels.color-scheme.delete-success-description` | EN has period, translation does not | `Successfully deleted {scheme}.` | `Bi serkeftî {scheme} hate jêbirin` |
| `panels.plugins.update-success` | Translation has period, EN does not | `Updated {plugin} to v{version}` | `{plugin} hate nûkirin bo v{version}.` |
| `toast.bluetooth.address-copied` | EN has period, translation does not | `Address copied to clipboard.` | `Navnîşan li clipboardê hate kopîkirin` |

---

### nl.json (3 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `common.disconnect` | Translation has period, EN does not | `Disconnect` | `Verbreek de verbinding.` |
| `panels.system-monitor.use-custom-highlight-colors-label` | Translation has period, EN does not | `Use custom highlight colors` | `Gebruik aangepaste markeerkleuren.` |
| `setup.welcome-note` | Translation has period, EN does not | `Just a few basics to get you started — full options are in the settings` | `Een paar basisinstellingen om je op weg te helpen – alle opties vind je in instellingen.` |

---

### pl.json (4 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `panels.desktop-widgets.edit-mode-controls-explanation` | EN has period, translation does not | `Left-click & drag: Move or resize the widget.\nRight-click: Open the context menu options.` | `Lewy przycisk myszy: Przesuń widżet\nPrawy przycisk myszy: Zmień rozmiar widżetu` |
| `panels.plugins.filter-tags-description` | Translation has period, EN does not | `Filter plugins by category or download status` | `Filtruj wtyczki według kategorii lub statusu pobierania.` |
| `panels.plugins.install-incompatible` | EN has period, translation does not | `{plugin} requires Noctalia v{version} or higher.` | `{plugin} wymaga Noctalii w wersji v{version} lub wyższej` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Obciąż. śr.` |

---

### pt.json (13 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.custom-button.right-click-update-text` | Translation has period, EN does not | `Update displayed text on right-click` | `Atualizar o texto exibido ao clicar com o botão direito.` |
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Use fonte monoespaçada para largura de caractere consistente.\n` |
| `bar.workspace.enable-scrollwheel-label` | Translation has period, EN does not | `Scroll to switch workspaces` | `Role para alternar entre áreas de trabalho.` |
| `common.none` | Translation has period, EN does not | `None` | `Nenhum.` |
| `display-modes.always-hide` | Translation has period, EN does not | `Always hide` | `Sempre se esconda.` |
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `Tempo em segundos para o título rolar do início ao fim` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `Ativar rolagem contínua para títulos de mídia longos` |
| `panels.bar.appearance-use-separate-opacity-label` | Translation has period, EN does not | `Use separate bar opacity` | `Usar opacidade separada para as barras.` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Mostrar ou ocultar o dock completamente` |
| `panels.launcher.settings-ignore-mouse-input-label` | Translation has period, EN does not | `Ignore mouse input` | `Ignorar entrada do mouse.` |
| `panels.location.date-time-use-analog-label` | Translation has period, EN does not | `Use analog style clock` | `Use um relógio de estilo analógico.` |
| `panels.plugins.available-no-plugins-label` | Translation has period, EN does not | `No plugins available` | `Nenhum plugin disponível.` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Carga méd.` |

---

### ru.json (7 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Используйте моноширинный шрифт для единообразной ширины символов.\n` |
| `bar.workspace.enable-scrollwheel-label` | Translation has period, EN does not | `Scroll to switch workspaces` | `Прокрутите, чтобы переключить рабочие столы.` |
| `display-modes.always-hide` | Translation has period, EN does not | `Always hide` | `Всегда прячься.` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Показать или скрыть док целиком` |
| `panels.plugins.available-no-plugins-label` | Translation has period, EN does not | `No plugins available` | `Нет доступных плагинов.` |
| `panels.plugins.filter-tags-description` | Translation has period, EN does not | `Filter plugins by category or download status` | `Фильтровать плагины по категории или статусу загрузки.` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Нaгр. ср.` |

---

### tr.json (11 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.system-monitor.use-monospace-font-description` | EN has period, translation does not | `Use monospace font for consistent character width.` | `Tekdüze karakter genişliği için tek aralıklı yazı tipini kullanın.\n` |
| `calendar.weather-loading` | Translation has period, EN does not | `Loading weather…` | `Hava durumu yükleniyor...` |
| `display-modes.always-hide` | Translation has period, EN does not | `Always hide` | `Her zaman saklan.` |
| `display-modes.always-show` | Translation has period, EN does not | `Always show` | `Daima göster.` |
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `Başlığın baştan sona kayması için saniye cinsinden süre` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `Uzun ortam başlıkları için sürekli kaydırmayı etkinleştirin` |
| `panels.desktop-widgets.media-player-enabled-label` | Translation has period, EN does not | `Enable media player widget` | `Medya oynatıcı widget'ını etkinleştir.` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Dock'u tamamen gösterin veya gizleyin` |
| `panels.launcher.settings-ignore-mouse-input-label` | Translation has period, EN does not | `Ignore mouse input` | `Fare girişini yoksay.` |
| `panels.plugins.update-incompatible` | Translation has period, EN does not | `Requires Noctalia v{version} or higher` | `Noctalia v{version} veya üzeri gerektirir.` |
| `tooltips.move-to-section` | Translation has period, EN does not | `Move to {section}` | `{section} bölümüne git.` |

---

### uk-UA.json (4 inconsistencies)

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `Час у секундах для прокрутки назви від початку до кінця` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `Увімкнути безперервну прокрутку для довгих назв медіа` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `Показати або сховати док повністю` |
| `system-monitor.load-average` | Translation has period, EN does not | `Load Avg` | `Нaгр. ср.` |

---

### zh-CN.json (7 inconsistencies)

**Note:** Chinese uses `。` (full-width period) which is checked alongside `.`

| Key | Issue | EN | Translation |
|-----|-------|-----|-------------|
| `bar.taskbar.only-active-workspaces-description` | EN has period, translation does not | `Show only apps from active workspaces.` | `仅显示来自活动工作区的应用程序` |
| `panels.audio.media-scrolling-speed-description` | EN has period, translation does not | `Time in seconds for the title to scroll from start to end.` | `标题从头到尾滚动所需的时间（秒）` |
| `panels.audio.media-scrolling-title-description` | EN has period, translation does not | `Enable continuous scrolling for long media titles.` | `为长媒体标题启用连续滚动` |
| `panels.color-scheme.templates-programs-description` | EN has period, translation does not | `Application-specific theming.` | `应用程序特定主题` |
| `panels.dock.enabled-description` | EN has period, translation does not | `Show or hide the dock entirely.` | `完全显示或隐藏停靠栏` |
| `panels.general.fonts-default-scale-description` | EN has period, translation does not | `Increase or decrease the size of the standard text.` | `增大或减小标准文本的尺寸` |
| `panels.general.fonts-monospace-scale-description` | EN has period, translation does not | `Increase or decrease the size of the monospaced text.` | `增大或减小等宽文本的尺寸` |

---

## Analysis Methodology

The analysis script:
1. Loads `en.json` as the reference baseline
2. Flattens all nested JSON structures into dot-notation keys
3. Compares each translation file against `en.json`
4. For `zh-CN.json` and `ja.json`, checks for both `.` and `。` (full-width period)
5. Reports any mismatches in period usage

## Generated By

This report was automatically generated by analyzing the translation files in `/Assets/Translations/`.
