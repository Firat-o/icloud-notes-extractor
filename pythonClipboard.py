import tkinter as tk
import os
import time

# ==========================================
# 1. ZIELPFAD DEFINIEREN
# Trage hier deinen Wunschpfad ein (z.B. r"D:\Backup\Notizen").
# Laesst du die Variable leer, wird automatisch ein Ordner 
# namens "Extracted_Notes" dort erstellt, wo das Skript liegt.
# ==========================================
zielpfad = r"" 

if zielpfad == "":
    backup_dir = os.path.join(os.getcwd(), "Extracted_Notes")
else:
    backup_dir = zielpfad

os.makedirs(backup_dir, exist_ok=True)

root = tk.Tk()
root.withdraw()

print("SYSTEM ONLINE: ueberwache zwischenablage...")
print(f"zielverzeichnis: {backup_dir}")

last_clipboard = ""

while True:
    try:
        current_clipboard = root.clipboard_get()
        
        if current_clipboard != last_clipboard and current_clipboard.strip() != "":
            last_clipboard = current_clipboard
            
            safe_name = "".join([c for c in current_clipboard[:20] if c.isalnum() or c in " _-"]).strip()
            if not safe_name:
                safe_name = "Notiz"
                
            filename = os.path.join(backup_dir, f"{safe_name}_{int(time.time())}.md")
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(current_clipboard)
            print(f"[+] extrahiert: {filename}")
            
    except tk.TclError:
        pass 
    
    time.sleep(0.5)
    root.update()