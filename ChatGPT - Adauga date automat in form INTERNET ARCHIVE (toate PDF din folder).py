import os
import time
import ctypes
import webbrowser
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

mouse = MouseController()
keyboard = KeyboardController()

def set_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

def write(text):
    keyboard.type(str(text))
    print(f"✍️ Scris: {text}")
    time.sleep(1)

def press_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# Coordonate (actualizate)
coords = {
    "upload_button": (790, 416),
    "file_path_field": (705, 728),
    "open_button": (986, 766),
    "description": (598, 379),
    "tags": (584, 590),
    "date_year": (419, 505),
    "date_mm": (476, 506),
    "date_dd": (552, 506),
    "collection": (486, 562),
    "upload_final": (714, 794)
}

# Dată implicită
year = "1987"
month = "08"
day = "17"

# Folder cu fișiere
pdf_folder = r"g:\De pus pe FTP 2\TEST"

def complete_upload_for_file(file_path):
    text_title = os.path.splitext(os.path.basename(file_path))[0]
    print(f"\n📂 Fișier: {file_path}")
    print(f"📄 Titlu extras: {text_title}")

    webbrowser.open_new_tab("https://archive.org/upload/")
    time.sleep(6)

    try:
        print("📌 PAS 1: Click Upload")
        set_mouse(*coords["upload_button"])
        mouse.click(Button.left)
        time.sleep(2)

        print("📌 PAS 2: Introducere cale fișier")
        set_mouse(*coords["file_path_field"])
        mouse.click(Button.left)
        time.sleep(1)
        write(file_path)
        press_enter()
        time.sleep(6)

        print("📌 PAS 3: Click Open")
        set_mouse(*coords["open_button"])
        mouse.click(Button.left)
        time.sleep(6)

        print("📌 PAS 4: Descriere")
        set_mouse(*coords["description"])
        mouse.click(Button.left)
        time.sleep(0.5)
        write(text_title)

        print("📌 PAS 5: Tags")
        set_mouse(*coords["tags"])
        mouse.click(Button.left)
        time.sleep(0.5)
        write(text_title)

        print("📌 PAS 6: Year")
        set_mouse(*coords["date_year"])
        mouse.click(Button.left)
        time.sleep(0.5)
        write(year)

        print("📌 PAS 7: Month")
        set_mouse(*coords["date_mm"])
        mouse.click(Button.left)
        time.sleep(0.3)
        set_mouse(*coords["date_mm"])
        write(month)

        print("📌 PAS 8: Day")
        set_mouse(*coords["date_dd"])
        mouse.click(Button.left)
        time.sleep(0.3)
        set_mouse(*coords["date_dd"])
        write(day)

        print("📌 PAS 9: Click Collection")
        set_mouse(*coords["collection"])
        mouse.click(Button.left)
        time.sleep(1)

        print("📌 PAS 10: Upload Final")
        set_mouse(*coords["upload_final"])
        mouse.click(Button.left)
        time.sleep(1)

        print("✅ Upload complet pentru: " + text_title)

    except Exception as e:
        print(f"❌ Eroare la fișierul {text_title}: {e}")

def main():
    pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ Nu s-au găsit fișiere PDF în folderul specificat.")
        return

    print(f"🔍 Găsite {len(pdf_files)} fișiere PDF. Începem upload-ul...")

    for idx, file_path in enumerate(pdf_files, 1):
        print(f"\n=== ÎNREGISTRAREA {idx} DIN {len(pdf_files)} ===")
        complete_upload_for_file(file_path)
        print("⏳ Pauză 4 secunde înainte de următorul fișier...")
        time.sleep(4)

    print("\n✅ Toate fișierele au fost procesate.")

if __name__ == "__main__":
    main()
