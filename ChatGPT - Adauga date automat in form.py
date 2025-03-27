import pandas as pd
import os
import webbrowser
import time
import ctypes
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

# Citire date din Excel
excel_path = r"E:\Carte\BB\17 - Site Leadership\alte\Ionel Balauta\Aryeht\Task 1 - Traduce tot site-ul\Doar Google Web\Andreea\Meditatii\2023\Internet Archive BEBE bun\Inspect elements\Test\1\date_formulare.xlsx"
html_path = r"E:\Carte\BB\17 - Site Leadership\alte\Ionel Balauta\Aryeht\Task 1 - Traduce tot site-ul\Doar Google Web\Andreea\Meditatii\2023\Internet Archive BEBE bun\Inspect elements\Test\1\form.html"

# Coordonate mouse precise (înregistrate manual cu scriptul anterior)
coords = [
    (506, 274),  # nume
    (507, 372),  # email
    (505, 460),  # telefon
    (505, 544),  # click combo categorie
    (530, 654),  # selectare categorie
    (531, 640),  # click combo subcategorie
    (536, 731),  # selectare subcategorie
    (536, 731),  # mesaj
    (467, 681),  # checkbox termeni
    (469, 727),  # checkbox newsletter
    (502, 771),  # submit
]

# Setare mouse și tastatură
mouse = MouseController()
keyboard = KeyboardController()

# Funcție nativă pentru mutarea mouse-ului (mai exactă decât pynput)
def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Click nativ
def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

# Scriere tastatură
def type_text(text):
    keyboard.type(text)

# Deschidere formular HTML
def open_html():
    url = 'file:///' + os.path.abspath(html_path).replace("\\", "/")
    webbrowser.open(url)

def scroll_down(lines=5):
    for _ in range(lines):
        mouse.scroll(0, -1)
        time.sleep(0.2)

def completeaza_formular():
    df = pd.read_excel(excel_path)
    row = df.iloc[0]

    open_html()
    time.sleep(3)

    valori = [
        row['nume'],
        row['email'],
        str(row['telefon']),
        '',  # click categorie
        '',  # categorie
        '',  # click subcategorie
        '',  # subcategorie
        row['mesaj']
    ]

    for i, val in enumerate(valori):
        move_mouse(*coords[i])
        time.sleep(0.3)
        mouse.click(Button.left)
        time.sleep(0.3)
        if val:
            type_text(str(val))
        time.sleep(0.5)

    scroll_down(5)
    time.sleep(1)

    move_mouse(*coords[8])  # Termeni
    time.sleep(0.3)
    mouse.click(Button.left)
    time.sleep(0.3)

    move_mouse(*coords[9])  # Newsletter
    time.sleep(0.3)
    mouse.click(Button.left)
    time.sleep(0.3)

    move_mouse(*coords[10])  # Submit
    time.sleep(0.3)
    mouse.click(Button.left)
    time.sleep(1)  # Așteaptă să apară alerta

    # Apasă ENTER pentru închiderea alertei
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    print("✅ Formular completat și alertă închisă.")


    print("✅ Formular completat cu succes!")

# Importuri lipsă
from pynput.mouse import Button

if __name__ == "__main__":
    completeaza_formular()
