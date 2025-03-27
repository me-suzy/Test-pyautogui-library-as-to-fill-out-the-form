import pyautogui
import time
import webbrowser
from datetime import datetime

# Configurări de bază
pyautogui.PAUSE = 1.0  # Pauză între acțiuni
pyautogui.FAILSAFE = True  # Oprire de siguranță

def print_status(mesaj):
    """Afișează un mesaj de status cu timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] >>> {mesaj}")

def countdown(seconds):
    """Afișează un countdown"""
    for i in range(seconds, 0, -1):
        print(f"Începe în {i}...")
        time.sleep(1)

def deschide_browser(url):
    """Deschide browser-ul la URL-ul specificat"""
    print_status(f"Deschid browser-ul la adresa: {url}")
    webbrowser.open(url)

    # Așteaptă să se încarce pagina
    print_status("Aștept încărcarea paginii...")
    time.sleep(3)  # Așteptăm 3 secunde pentru încărcarea paginii

def automatizare_formular_complet(url, date_intrare=None):
    """
    Automatizează complet procesul de completare a formularului
    folosind TAB pentru a selecta primul câmp

    Args:
        url: URL-ul formularului
        date_intrare: Un dicționar cu datele de intrare (opțional)
    """
    # Valorile implicite pentru formular
    date_implicite = {
        'nume': 'Ion Popescu',
        'email': 'ion.popescu@email.com',
        'telefon': '0712345678',
        'categorie': 'Profesional',
        'subcategorie': 'Vânzări',
        'mesaj': 'Acesta este un mesaj de test pentru formularul automatizat.'
    }

    # Folosim datele de intrare sau valorile implicite
    date = date_intrare if date_intrare else date_implicite

    # Deschide browser-ul
    deschide_browser(url)

    try:
        # Folosim TAB pentru a selecta primul câmp din formular
        print_status("Selectare primul câmp folosind tasta TAB")
        pyautogui.press('tab')
        time.sleep(1)  # Pauză după apăsarea tastei TAB

        # Verificăm dacă am selectat primul câmp (opțional - nu avem cum să știm sigur)
        print_status("Primul câmp ar trebui să fie selectat acum")

        # Completare Nume
        print_status("Completare câmp Nume")
        pyautogui.typewrite(date['nume'])
        time.sleep(0.5)

        # Navigare și completare Email
        print_status("Navigare și completare câmp Email")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite(date['email'])
        time.sleep(0.5)

        # Navigare și completare Telefon
        print_status("Navigare și completare câmp Telefon")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite(date['telefon'])
        time.sleep(0.5)

        # Navigare și selectare Categorie
        print_status("Navigare la dropdown Categorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Deschidere dropdown Categorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        # Selectăm "Profesional" (presupunem că necesită 2 apăsări P)
        print_status(f"Selectare '{date['categorie']}' din Categorie")
        if date['categorie'] == 'Profesional':
            pyautogui.press('p')  # Prima apăsare P
            time.sleep(0.3)
            pyautogui.press('p')  # A doua apăsare P
        elif date['categorie'] == 'Personal':
            pyautogui.press('p')  # O singură apăsare P
        elif date['categorie'] == 'Educație':
            pyautogui.press('e')  # Apăsare E
        elif date['categorie'] == 'Altele':
            pyautogui.press('a')  # Apăsare A

        time.sleep(0.5)
        pyautogui.press('enter')  # Confirmă selecția
        time.sleep(0.5)

        # Navigare și selectare Subcategorie
        print_status("Navigare la dropdown Subcategorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Deschidere dropdown Subcategorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        # Selectăm subcategoria specificată
        print_status(f"Selectare '{date['subcategorie']}' din Subcategorie")
        prima_litera = date['subcategorie'][0].lower()
        pyautogui.press(prima_litera)
        time.sleep(0.5)
        pyautogui.press('enter')  # Confirmă selecția
        time.sleep(0.5)

        # Navigare și completare Mesaj
        print_status("Navigare și completare câmp Mesaj")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite(date['mesaj'])
        time.sleep(0.5)

        # Bifare checkbox-uri
        print_status("Navigare și bifare checkbox Termeni")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('space')  # Bifare Termeni
        time.sleep(0.5)

        print_status("Navigare și bifare checkbox Newsletter")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('space')  # Bifare Newsletter
        time.sleep(0.5)

        # Trimitere formular
        print_status("Navigare la butonul Trimite")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Apăsare buton Trimite")
        pyautogui.press('enter')  # Apăsare buton Trimite
        time.sleep(1)

        print_status("FORMULAR TRIMIS CU SUCCES!")

        # Închidere mesaj de confirmare
        print_status("Așteptare și închidere mesaj de confirmare")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        # Resetare formular
        print_status("Navigare la butonul Resetează")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Apăsare buton Resetează")
        pyautogui.press('enter')  # Apăsare buton Resetează
        time.sleep(1)

        print_status("FORMULAR RESETAT CU SUCCES!")
        return True

    except Exception as e:
        print_status(f"EROARE: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== AUTOMATIZARE COMPLETĂ FORMULAR CU TAB ===")

    try:
        # URL-ul formularului
        url_formular = "file:///E:/Carte/BB/17%20-%20Site%20Leadership/alte/Ionel%20Balauta/Aryeht/Task%201%20-%20Traduce%20tot%20site-ul/Doar%20Google%20Web/Andreea/Meditatii/2023/Internet%20Archive%20BEBE%20bun/Inspect%20elements/Test/1/form.html"

        print("Acest script va:")
        print("1. Deschide automat browser-ul cu formularul")
        print("2. Folosește tasta TAB pentru a selecta primul câmp")
        print("3. Completează toate câmpurile formularului")
        print("4. Trimite și resetează formularul")
        print()
        print("Nu trebuie să faci click manual pe primul câmp!")
        print()

        input("Apasă Enter pentru a începe...")
        countdown(3)
        automatizare_formular_complet(url_formular)

    except KeyboardInterrupt:
        print("\nScript oprit de utilizator.")