# icloud-notes-extractor

**Das Problem:**
Es gibt aktuell keine *mir bekannte* schnelle Möglichkeit, alle iCloud Notizen auf einmal zu exportieren. Die offizielle DSGVO-Datenanfrage bei Apple dauert mehrere Tage. Web-Scraping (z.B. mit Selenium) im Browser zu nutzen, riskiert Blockaden durch Apples Anti-Bot-Systeme.

**Die Lösung:**
Ein simples Python-Skript, das im Hintergrund läuft und die lokale Zwischenablage überwacht. Man geht die Notizen manuell im Browser durch, kopiert sie, und das Skript erstellt automatisch saubere Markdown-Dateien (.md) im Zielordner.

### Anleitung (Steps)

1. Repo klonen oder das Skript herunterladen.
2. **Pfad anpassen (Optional):** Öffne `pythonClipboard.py` im Editor. Trage oben bei `zielpfad` deinen gewünschten Speicherort ein (z. B. `zielpfad = r"C:\Backup\Notizen"`). Lässt du das Feld leer, wird automatisch ein Ordner im Verzeichnis des Skripts erstellt.
3. Terminal öffnen und das Skript ausführen: `python pythonClipboard.py`
4. Im Browser `icloud.com/notes` öffnen.
5. Erste Notiz anklicken, in den Text klicken, `Strg + A` (alles markieren) und `Strg + C` (kopieren) drücken.
6. Das Terminal bestätigt das Speichern. Direkt zur nächsten Notiz gehen und den Vorgang wiederholen.
7. Wenn alle Notizen kopiert sind: Im Terminal `Strg + C` drücken, um den Prozess zu beenden.
