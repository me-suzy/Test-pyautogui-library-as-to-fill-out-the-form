import pyautogui
import time

# Configurări de bază
pyautogui.PAUSE = 1.0  # Pauză între acțiuni
pyautogui.FAILSAFE = True  # Oprire de siguranță

def print_status(mesaj):
    """Afișează un mesaj de status"""
    print(f">>> {mesaj}")

def countdown(seconds):
    """Afișează un countdown"""
    for i in range(seconds, 0, -1):
        print(f"Începe în {i}...")
        time.sleep(1)

def automatizare_formular(test_reset=True):
    """
    Automatizează completarea formularului
    Folosește metoda TAB pentru navigare și prima literă pentru dropdown-uri

    Args:
        test_reset: Dacă este True, va testa și butonul de resetare după trimitere
    """
    print_status("PREGĂTIRE AUTOMATIZARE FORMULAR")
    print_status("Click manual pe primul câmp (Nume) înainte de a începe")
    countdown(5)

    try:
        # ---------- Completare Nume ----------
        print_status("Completare câmp Nume")
        pyautogui.typewrite("Ion Popescu")
        time.sleep(0.5)

        # ---------- Completare Email ----------
        print_status("Navigare și completare câmp Email")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite("ion.popescu@email.com")
        time.sleep(0.5)

        # ---------- Completare Telefon ----------
        print_status("Navigare și completare câmp Telefon")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite("0712345678")
        time.sleep(0.5)

        # ---------- Selectare Categorie ----------
        print_status("Navigare la dropdown Categorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Deschidere dropdown Categorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        print_status("Selectare 'Profesional' din Categorie (tasta P de 2 ori)")
        pyautogui.press('p')  # Prima apăsare P
        time.sleep(0.3)
        pyautogui.press('p')  # A doua apăsare P pentru a ajunge la "Profesional"
        time.sleep(0.5)
        pyautogui.press('enter')  # Confirmă selecția
        time.sleep(0.5)

        # ---------- Selectare Subcategorie ----------
        print_status("Navigare la dropdown Subcategorie")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Deschidere dropdown Subcategorie")
        pyautogui.press('space')  # Deschide dropdown-ul
        time.sleep(0.5)

        print_status("Selectare 'Vânzări' din Subcategorie (tasta V)")
        pyautogui.press('v')  # Apasă V pentru "Vânzări"
        time.sleep(0.5)
        pyautogui.press('enter')  # Confirmă selecția
        time.sleep(0.5)

        # ---------- Completare Mesaj ----------
        print_status("Navigare și completare câmp Mesaj")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.typewrite("Acesta este un mesaj de test pentru formularul automatizat.")
        time.sleep(0.5)

        # ---------- Bifare Checkbox Termeni ----------
        print_status("Navigare și bifare checkbox Termeni")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('space')  # Bifează checkbox-ul
        time.sleep(0.5)

        # ---------- Bifare Checkbox Newsletter ----------
        print_status("Navigare și bifare checkbox Newsletter")
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('space')  # Bifează checkbox-ul
        time.sleep(0.5)

        # ---------- Apăsare Buton Trimite ----------
        print_status("Navigare la butonul Trimite")
        pyautogui.press('tab')
        time.sleep(0.5)

        print_status("Apăsare buton Trimite")
        pyautogui.press('enter')
        time.sleep(1)

        print_status("FORMULAR TRIMIS CU SUCCES!")

        # ---------- Închidere mesaj de confirmare ----------
        print_status("Așteptare mesaj de confirmare")
        time.sleep(1)

        print_status("Închidere mesaj de confirmare cu Enter")
        pyautogui.press('enter')
        time.sleep(1)

        # ---------- Test buton Resetează ----------
        if test_reset:
            print_status("TESTARE BUTON RESETEAZĂ")

            print_status("Navigare la butonul Resetează folosind Tab")
            pyautogui.press('tab')  # Navigare la butonul Resetează
            time.sleep(0.5)

            print_status("Apăsare buton Resetează")
            pyautogui.press('enter')
            time.sleep(1)

            print_status("FORMULAR RESETAT CU SUCCES!")
            print_status("Verificare: Toate câmpurile ar trebui să fie goale acum.")

    except Exception as e:
        print(f"EROARE: {str(e)}")

if __name__ == "__main__":
    print("=== SCRIPT SIMPLU PENTRU AUTOMATIZARE FORMULAR ===")
    print("1. Deschide formularul în browser")
    print("2. Asigură-te că formularul este complet vizibil")
    print("3. Când ești gata, apasă Enter pentru a începe")
    print()
    print("Acest script va:")
    print("- Completa toate câmpurile din formular")
    print("- Selecta 'Profesional' din dropdown-ul Categorie")
    print("- Selecta 'Vânzări' din dropdown-ul Subcategorie")
    print("- Testa atât butonul Trimite cât și butonul Resetează")

    input("Apasă Enter pentru a continua...")

    automatizare_formular(test_reset=True)