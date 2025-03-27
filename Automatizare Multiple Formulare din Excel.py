import pyautogui
import time
import webbrowser
import pandas as pd
from datetime import datetime

# Configurări de bază
pyautogui.PAUSE = 1.0  # Pauză între acțiuni
pyautogui.FAILSAFE = True  # Oprire de siguranță

# Calea către fișierul Excel și URL-ul formularului (hardcodate)
EXCEL_FILE = r"e:\Carte\BB\17 - Site Leadership\alte\Ionel Balauta\Aryeht\Task 1 - Traduce tot site-ul\Doar Google Web\Andreea\Meditatii\2023\Internet Archive BEBE bun\Inspect elements\Test\1\date_formulare.xlsx"
FORM_URL = r"file:///E:/Carte/BB/17%20-%20Site%20Leadership/alte/Ionel%20Balauta/Aryeht/Task%201%20-%20Traduce%20tot%20site-ul/Doar%20Google%20Web/Andreea/Meditatii/2023/Internet%20Archive%20BEBE%20bun/Inspect%20elements/Test/1/form.html"

# Numărul de înregistrări de procesat (implicit toate din Excel)
MAX_ENTRIES = None  # None înseamnă toate înregistrările

def print_status(mesaj):
    """Afișează un mesaj de status cu timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] >>> {mesaj}")

def citeste_date_excel():
    """Citește datele din Excel"""
    try:
        print_status(f"Citesc datele din Excel")
        # Încercăm să citim Excel-ul
        df = pd.read_excel(EXCEL_FILE)

        # Luăm înregistrările specificate
        if MAX_ENTRIES is not None:
            df = df.head(MAX_ENTRIES)

        # Convertim DataFrame-ul în listă de dicționare
        date_lista = df.to_dict('records')

        print_status(f"S-au citit {len(date_lista)} înregistrări din Excel")
        return date_lista

    except Exception as e:
        print_status(f"EROARE la citirea Excel: {str(e)}")
        return []

def deschide_browser():
    """Deschide browser-ul la URL-ul formularului"""
    print_status(f"Deschid formularul în browser")
    webbrowser.open(FORM_URL)

    # Așteaptă să se încarce pagina
    print_status("Aștept încărcarea paginii...")
    time.sleep(3)

def selecteaza_primul_camp(prima_data=False):
    """
    Selectează primul câmp din formular folosind TAB

    Args:
        prima_data: True dacă este prima dată când selectăm, False după resetare
    """
    if prima_data:
        # Prima dată, apăsăm TAB o singură dată
        print_status("Selectez primul câmp cu TAB")
        pyautogui.press('tab')
        time.sleep(0.5)
    else:
        # După resetare, apăsăm TAB de 5 ori pentru a ajunge la primul câmp
        print_status("Navighez înapoi la primul câmp (5x TAB)")
        for i in range(5):
            pyautogui.press('tab')
            time.sleep(0.3)  # Pauză scurtă între apăsări

def completeaza_formular(date, index):
    """Completează formularul cu datele specificate"""
    print_status(f"Completez formularul cu datele înregistrării #{index+1}: {date['nume']}")

    try:
        # Selectăm primul câmp
        selecteaza_primul_camp(prima_data=(index == 0))
        time.sleep(0.5)

        # Completare Nume
        print_status(f"Completare Nume: {date['nume']}")
        pyautogui.typewrite(str(date['nume']))
        time.sleep(0.5)

        # Email
        print_status(f"Navigare la Email")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status(f"Completare Email: {date['email']}")
        pyautogui.typewrite(str(date['email']))
        time.sleep(0.5)

        # Telefon
        print_status(f"Navigare la Telefon")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status(f"Completare Telefon: {date['telefon']}")
        pyautogui.typewrite(str(date['telefon']))
        time.sleep(0.5)

        # Categorie
        print_status(f"Navigare la Categorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        # Mapăm categoriile la numărul de apăsări de taste
        categorie_map = {
            'personal': {'tasta': 'p', 'apasari': 1},
            'profesional': {'tasta': 'p', 'apasari': 2},
            'educație': {'tasta': 'e', 'apasari': 1},
            'educatie': {'tasta': 'e', 'apasari': 1},
            'altele': {'tasta': 'a', 'apasari': 1}
        }

        cat = str(date['categorie']).lower()
        if cat in categorie_map:
            tasta = categorie_map[cat]['tasta']
            apasari = categorie_map[cat]['apasari']
        else:
            # Dacă categoria nu e cunoscută, folosim prima literă
            tasta = cat[0]
            apasari = 1

        print_status(f"Deschid dropdown Categorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        print_status(f"Selectez '{date['categorie']}' cu tasta '{tasta}' (x{apasari})")
        for i in range(apasari):
            pyautogui.press(tasta)
            time.sleep(0.3)

        print_status(f"Confirm selecția cu Enter")
        pyautogui.press('enter')
        time.sleep(0.5)

        # Subcategorie
        print_status(f"Navigare la Subcategorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        # Mapăm subcategoriile la numărul de apăsări de taste
        subcategorie_map = {
            'hobby': {'tasta': 'h', 'apasari': 1},
            'sănătate': {'tasta': 's', 'apasari': 1},
            'sanatate': {'tasta': 's', 'apasari': 1},
            'familie': {'tasta': 'f', 'apasari': 1},
            'sport': {'tasta': 's', 'apasari': 2},  # A doua opțiune cu S
            'călătorii': {'tasta': 'c', 'apasari': 1},
            'calatorii': {'tasta': 'c', 'apasari': 1},
            'programare': {'tasta': 'p', 'apasari': 1},
            'design': {'tasta': 'd', 'apasari': 1},
            'marketing': {'tasta': 'm', 'apasari': 1},
            'vânzări': {'tasta': 'v', 'apasari': 1},
            'vanzari': {'tasta': 'v', 'apasari': 1}
        }

        subcat = str(date['subcategorie']).lower()
        if subcat in subcategorie_map:
            tasta = subcategorie_map[subcat]['tasta']
            apasari = subcategorie_map[subcat]['apasari']
        else:
            # Dacă subcategoria nu e cunoscută, folosim prima literă
            tasta = subcat[0]
            apasari = 1

        print_status(f"Deschid dropdown Subcategorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        print_status(f"Selectez '{date['subcategorie']}' cu tasta '{tasta}' (x{apasari})")
        for i in range(apasari):
            pyautogui.press(tasta)
            time.sleep(0.3)

        print_status(f"Confirm selecția cu Enter")
        pyautogui.press('enter')
        time.sleep(0.5)

        # Mesaj
        print_status(f"Navigare la Mesaj")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status(f"Completare Mesaj: {date['mesaj']}")
        pyautogui.typewrite(str(date['mesaj']))
        time.sleep(0.5)

        # Bifare checkbox-uri
        print_status(f"Navigare la checkbox Termeni")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status("Bifare checkbox Termeni")
        pyautogui.press('space')
        time.sleep(0.5)

        print_status(f"Navigare la checkbox Newsletter")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status("Bifare checkbox Newsletter")
        pyautogui.press('space')
        time.sleep(0.5)

        # Trimitere formular
        print_status(f"Navigare la butonul Trimite")
        pyautogui.press('tab')
        time.sleep(0.5)
        print_status("Apăsare buton Trimite")
        pyautogui.press('enter')
        time.sleep(1)

        print_status("FORMULAR TRIMIS CU SUCCES!")

        # Închidere mesaj de confirmare
        print_status("Închidere mesaj confirmare")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        if index < len(date) - 1:  # Dacă nu este ultima înregistrare
            # Resetează formularul pentru următoarea înregistrare
            print_status("Navigare la butonul Resetează")
            pyautogui.press('tab')
            time.sleep(0.5)
            print_status("Apăsare buton Resetează")
            pyautogui.press('enter')  # Apăsare buton Reset
            time.sleep(1)

        return True

    except Exception as e:
        print_status(f"EROARE la completarea formularului: {str(e)}")
        return False

def automatizare_completa():
    """Rulează întregul proces de automatizare"""
    print_status("=== ÎNCEPE AUTOMATIZAREA FORMULARULUI DIN EXCEL ===")

    # Citim datele din Excel
    date = citeste_date_excel()

    if not date:
        print_status("Nu s-au putut citi date din Excel. Automatizarea a eșuat.")
        return

    # Deschidem browser-ul
    deschide_browser()

    # Procesăm fiecare înregistrare
    for i, date_intrare in enumerate(date):
        # Completăm formularul
        succes = completeaza_formular(date_intrare, i)

        if succes:
            print_status(f"Înregistrarea #{i+1}/{len(date)} procesată cu succes")
        else:
            print_status(f"Eroare la procesarea înregistrării #{i+1}/{len(date)}")

        # Pauză între înregistrări (dacă nu este ultima)
        if i < len(date) - 1:
            print_status("Pauză înainte de următoarea înregistrare...")
            time.sleep(2)

    print_status("=== AUTOMATIZARE FINALIZATĂ ===")
    print_status(f"S-au procesat {len(date)} înregistrări")

if __name__ == "__main__":
    print("=== AUTOMATIZARE FORMULAR DIN EXCEL ===")
    if MAX_ENTRIES:
        print(f"Se vor procesa primele {MAX_ENTRIES} înregistrări din Excel")
    else:
        print("Se vor procesa toate înregistrările din Excel")

    print("Script pornit...")

    try:
        automatizare_completa()
    except KeyboardInterrupt:
        print_status("Script oprit de utilizator")