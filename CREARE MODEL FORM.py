import pyautogui
import time
import json
import os

# Configurarea pentru a face scriptul mai sigur
pyautogui.PAUSE = 0.5  # Pauză între acțiuni
pyautogui.FAILSAFE = True  # Dacă mutați mouse-ul în colțul din stânga sus, scriptul se oprește

def get_screen_info():
    """Obține informații despre ecran și afișează-le"""
    width, height = pyautogui.size()
    print(f"Rezoluție ecran: {width}x{height}")
    return width, height

def adapt_coordinates(x_percent, y_percent):
    """
    Convertește coordonatele procentuale în coordonate absolute
    bazate pe rezoluția ecranului.
    """
    width, height = pyautogui.size()
    x = int((x_percent / 100) * width)
    y = int((y_percent / 100) * height)
    return x, y

def click_relative(x_percent, y_percent, clicks=1, interval=0.0, button='left'):
    """Click la o poziție relativă pe ecran (în procente)"""
    x, y = adapt_coordinates(x_percent, y_percent)
    print(f"Click la poziția: {x},{y} (original: {x_percent}%,{y_percent}%)")
    pyautogui.click(x, y, clicks=clicks, interval=interval, button=button)

def type_text(text, interval=0.05):
    """Tastează text cu un interval între caractere"""
    pyautogui.typewrite(text, interval=interval)

def press_key(key):
    """Apasă o tastă"""
    pyautogui.press(key)

def scroll_down(clicks=5):
    """Derulează în jos"""
    pyautogui.scroll(-clicks)  # Valori negative pentru defilare în jos

def countdown(seconds):
    """Afișează un countdown"""
    for i in range(seconds, 0, -1):
        print(f"Începe în {i}...")
        time.sleep(1)

def capturare_coordonate():
    """Instrumentul de capturare a coordonatelor"""
    print("\n=== INSTRUMENT DE CAPTURARE COORDONATE ===")
    print("Acest instrument vă ajută să capturați coordonatele elementelor formularului.")
    print("Pentru fiecare element, poziționați mouse-ul și așteptați timpul specificat.")

    # Lista de elemente pentru care dorim să capturăm coordonate
    elemente = [
        "Câmp Nume",
        "Câmp Email",
        "Câmp Telefon",
        "Dropdown Categorie",
        "Opțiune Personal din Categorie",
        "Dropdown Subcategorie",
        "Opțiune Programare din Subcategorie",
        "Textarea Mesaj",
        "Checkbox Termeni",
        "Checkbox Newsletter",
        "Buton Trimite",
        "Buton Resetează"
    ]

    coordonate = {}

    print("\nPregatit pentru capturare...")
    time.sleep(2)

    for element in elemente:
        input(f"\nPoziționați mouse-ul peste '{element}' și apăsați Enter...")
        x, y = pyautogui.position()
        width, height = pyautogui.size()
        x_percent = round((x / width) * 100, 2)
        y_percent = round((y / height) * 100, 2)

        coordonate[element.lower().replace(" ", "_")] = (x_percent, y_percent)
        print(f"{element}: {x_percent}%, {y_percent}% ({x}, {y})")

    # Salvare coordonate în fișier JSON
    with open('coordonate_formular.json', 'w') as f:
        json.dump(coordonate, f, indent=4)

    print("\nCoordonate salvate în fișierul 'coordonate_formular.json'")
    return coordonate

def completeaza_formular_test(coord=None):
    """Completează formularul de test cu date"""
    if coord is None:
        # Încearcă să încarce coordonatele din fișier
        if os.path.exists('coordonate_formular.json'):
            with open('coordonate_formular.json', 'r') as f:
                coord = json.load(f)
        else:
            print("Nu s-au găsit coordonate salvate. Folosim valori implicite.")
            coord = {}

    # Obține și afișează informații despre ecran
    width, height = get_screen_info()

    # Așteaptă ca utilizatorul să pregătească fereastra browserului
    print("Pregătiți fereastra formularului...")
    print("Asigurați-vă că formularul HTML este încărcat și vizibil.")
    countdown(5)

    try:
        # Completare nume
        click_relative(
            *coord.get('câmp_nume', (50, 25))  # Valori implicite dacă nu există în fișier
        )
        type_text("Ion Popescu")

        # Completare email
        click_relative(
            *coord.get('câmp_email', (50, 30))
        )
        type_text("ion.popescu@email.com")

        # Completare telefon
        click_relative(
            *coord.get('câmp_telefon', (50, 35))
        )
        type_text("0712345678")

        # Selectare categorie
        click_relative(
            *coord.get('dropdown_categorie', (50, 42))
        )
        time.sleep(0.5)
        click_relative(
            *coord.get('opțiune_personal_din_categorie', (50, 47))
        )

        # Selectare subcategorie
        click_relative(
            *coord.get('dropdown_subcategorie', (50, 52))
        )
        time.sleep(0.5)
        click_relative(
            *coord.get('opțiune_programare_din_subcategorie', (50, 57))
        )

        # Scroll down pentru a vedea restul formularului
        scroll_down()
        time.sleep(0.5)

        # Completare mesaj
        click_relative(
            *coord.get('textarea_mesaj', (50, 65))
        )
        type_text("Acesta este un mesaj de test pentru automatizarea formularului. Scriptul PyAutoGUI funcționează corect!")

        # Bifare checkbox termeni
        click_relative(
            *coord.get('checkbox_termeni', (15, 75))
        )

        # Bifare checkbox newsletter
        click_relative(
            *coord.get('checkbox_newsletter', (15, 80))
        )

        # Apăsare buton trimite
        click_relative(
            *coord.get('buton_trimite', (35, 85))
        )

        print("\nFormular completat cu succes!")

    except Exception as e:
        print(f"Eroare la completarea formularului: {e}")

def main():
    """Funcția principală"""
    print("=== AUTOMATIZARE FORMULAR DE TEST ===")
    print("1. Capturare coordonate formular")
    print("2. Completare automată formular (folosind coordonate salvate)")
    print("0. Ieșire")

    alegere = input("\nAlegeți o opțiune: ")

    if alegere == "1":
        coordonate = capturare_coordonate()
        input("Apăsați Enter pentru a continua...")
        main()
    elif alegere == "2":
        completeaza_formular_test()
    elif alegere == "0":
        print("La revedere!")
    else:
        print("Opțiune invalidă!")
        main()

if __name__ == "__main__":
    main()