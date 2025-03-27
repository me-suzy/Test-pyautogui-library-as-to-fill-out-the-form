import pandas as pd
import os
import webbrowser
import time
import ctypes
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

# Căi fișiere
excel_path = r"E:\Carte\BB\17 - Site Leadership\alte\Ionel Balauta\Aryeht\Task 1 - Traduce tot site-ul\Doar Google Web\Andreea\Meditatii\2023\Internet Archive BEBE bun\Inspect elements\Test\1\date_formulare.xlsx"
html_path = r"E:\Carte\BB\17 - Site Leadership\alte\Ionel Balauta\Aryeht\Task 1 - Traduce tot site-ul\Doar Google Web\Andreea\Meditatii\2023\Internet Archive BEBE bun\Inspect elements\Test\1\form.html"

# Coordonate mouse (înregistrate)
coords = [
    (506, 274),  # nume
    (507, 372),  # email
    (505, 460),  # telefon
    (505, 544),  # click categorie
    (530, 654),  # selectare categorie
    (531, 640),  # click subcategorie
    (536, 731),  # selectare subcategorie
    (536, 731),  # mesaj
    (467, 681),  # checkbox termeni
    (469, 727),  # checkbox newsletter
    (502, 771),  # submit
]

# Setup control
mouse = MouseController()
keyboard = KeyboardController()

def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

def scroll_down(lines=5):
    for _ in range(lines):
        mouse.scroll(0, -1)
        time.sleep(0.2)

def type_text(text):
    keyboard.type(str(text))

def open_html():
    url = 'file:///' + os.path.abspath(html_path).replace("\\", "/")
    webbrowser.open_new_tab(url)

def completeaza_toate_formularele():
    df = pd.read_excel(excel_path)

    for idx, row in df.iterrows():
        print(f"\n===== ÎNREGISTRAREA {idx + 1} DIN {len(df)} =====")
        print(f"Nume:         {row['nume']}")
        print(f"Email:        {row['email']}")
        print(f"Telefon:      {row['telefon']}")
        print(f"Categorie:    {row['categorie']}")
        print(f"Subcategorie: {row['subcategorie']}")
        print(f"Mesaj:        {row['mesaj']}")
        print("====================================")

        # Deschide formularul
        open_html()
        time.sleep(3)

        # Completare câmpuri
        move_mouse(*coords[0])
        mouse.click(Button.left)
        time.sleep(0.3)
        type_text(row['nume'])
        time.sleep(1)

        move_mouse(*coords[1])
        mouse.click(Button.left)
        time.sleep(0.3)
        type_text(row['email'])
        time.sleep(1)

        move_mouse(*coords[2])
        mouse.click(Button.left)
        time.sleep(0.3)
        type_text(str(row['telefon']))
        time.sleep(1)

        move_mouse(*coords[3])
        mouse.click(Button.left)
        time.sleep(0.5)
        move_mouse(*coords[4])
        mouse.click(Button.left)
        time.sleep(1)

        move_mouse(*coords[5])
        mouse.click(Button.left)
        time.sleep(0.5)
        move_mouse(*coords[6])
        mouse.click(Button.left)
        time.sleep(1)

        move_mouse(*coords[7])
        mouse.click(Button.left)
        time.sleep(0.3)
        type_text(row['mesaj'])
        time.sleep(1)

        scroll_down(5)
        time.sleep(1)

        move_mouse(*coords[8])
        mouse.click(Button.left)
        time.sleep(1)

        move_mouse(*coords[9])
        mouse.click(Button.left)
        time.sleep(1)

        move_mouse(*coords[10])
        mouse.click(Button.left)
        time.sleep(1)

        # Închide alertă
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("✅ Formular trimis și alertă închisă.")

if __name__ == "__main__":
    completeaza_toate_formularele()
