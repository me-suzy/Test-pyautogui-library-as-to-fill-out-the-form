import os
import time
import ctypes
import shutil
import webbrowser
import re
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

# Coordonate
coords = {
    "upload_button": (790, 416),
    "file_path_field": (705, 728),
    "open_button": (986, 766),
    "description": (598, 379),
    "tags": (474, 440),     # (438, 617),
    "date_year": (398, 531),
    "date_mm": (461, 546),
    "date_dd": (528, 546),
    "collection": (476, 579),
    "upload_final": (765, 812)
}



# Config
base_dir = r"g:\ARHIVA\M"
fallback_dir = r"d:\3"
upload_exts = [".pdf", ".epub", ".mobi", ".docx", ".doc", ".rtf", ".djvu"]
fallback_priority = [".epub", ".mobi", ".docx", ".doc", ".rtf", ".djvu"]
year, month, day = "1987", "08", "17"

# Subfolder de start și stop
start_from = "McInthyre, Elizabeth+++"
stop_at = "McMaster Bujold, Lois+++"

def natural_sort_key(s):
    """Funcție pentru sortarea naturală a șirurilor"""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]

def find_all_files_recursively(folder_path):
    """Găsește toate fișierele recursiv în folderul specificat și subfoldere"""
    all_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)

    return all_files

def upload_to_archive(file_list, title):
    joined_files = '"{}"'.format('" "'.join(file_list))  # Corect pentru upload
    print(f"\n🌐 Uploadăm: {title}")
    print(f"🗂️ Fișiere: {joined_files}")

    webbrowser.open_new_tab("https://archive.org/upload/")
    time.sleep(6)

    try:
        set_mouse(*coords["upload_button"])
        mouse.click(Button.left)
        time.sleep(6)

        set_mouse(*coords["file_path_field"])
        mouse.click(Button.left)
        time.sleep(1)
        write(joined_files)
        press_enter()
        time.sleep(6)

        set_mouse(*coords["open_button"])
        mouse.click(Button.left)
        time.sleep(6)

        # Fill in tags
        set_mouse(*coords["tags"])
        mouse.click(Button.left)
        write(title)

        # Fill in date fields
        set_mouse(*coords["date_year"])
        mouse.click(Button.left)
        write(year)

        set_mouse(*coords["date_mm"])
        mouse.click(Button.left)
        set_mouse(*coords["date_mm"])
        write(month)

        set_mouse(*coords["date_dd"])
        mouse.click(Button.left)
        set_mouse(*coords["date_dd"])
        write(day)

        # Click on collection first
        set_mouse(*coords["collection"])
        mouse.click(Button.left)
        time.sleep(1)

        # CHANGED: Now fill description after collection
        set_mouse(*coords["description"])
        mouse.click(Button.left)
        write(title)

        # Finally click upload
        set_mouse(*coords["upload_final"])
        mouse.click(Button.left)
        print(f"✅ Upload complet: {title}")

    except Exception as e:
        print(f"❌ Eroare upload {title}: {e}")

def fallback_copy(files, title):
    """Copiază fișiere în folderul de fallback conform priorității"""
    if not files:
        return False

    # Sortăm fișierele bazat pe prioritate
    for ext in fallback_priority:
        for file in files:
            if file.lower().endswith(ext):
                dest = os.path.join(fallback_dir, os.path.basename(file))
                shutil.copy(file, dest)
                print(f"📥 Fallback copiat: {file} → {dest}")
                return True

    # Dacă nu găsim niciun fișier prioritar, copiem primul fișier
    dest = os.path.join(fallback_dir, os.path.basename(files[0]))
    shutil.copy(files[0], dest)
    print(f"📥 Fallback copiat (ultimă opțiune): {files[0]} → {dest}")
    return True

def process_all_folders():
    if not os.path.exists(fallback_dir):
        os.makedirs(fallback_dir)

    # Obține toate folderele din directorul de bază
    all_folders = [entry.name for entry in os.scandir(base_dir) if entry.is_dir()]

    # Sortează folderele alfabetic - asigură ordinea naturală
    all_folders.sort(key=natural_sort_key)

    # Găsește pozițiile de start și stop
    try:
        start_index = all_folders.index(start_from)
    except ValueError:
        print(f"❌ Folderul de start '{start_from}' nu a fost găsit.")
        return

    try:
        stop_index = all_folders.index(stop_at)
    except ValueError:
        print(f"❌ Folderul final '{stop_at}' nu a fost găsit.")
        return

    if start_index > stop_index:
        print("⚠️ Ordinea este greșită: start este DUPĂ stop.")
        return

    # Selectăm doar folderele între start și stop (inclusiv)
    target_folders = all_folders[start_index:stop_index + 1]

    print(f"📂 Se vor procesa {len(target_folders)} foldere:")
    for i, folder in enumerate(target_folders, 1):
        print(f"  {i}. {folder}")

    print("\n🚀 Începe procesarea...")

    for folder_idx, folder_name in enumerate(target_folders, 1):
        folder_path = os.path.join(base_dir, folder_name)
        print(f"\n📁 [{folder_idx}/{len(target_folders)}] Procesez: {folder_name}")

        # Verifică dacă folderul există
        if not os.path.exists(folder_path):
            print(f"⚠️ Folderul '{folder_name}' nu există, se sare peste.")
            continue

        # Obține toate fișierele din folder ȘI din subfoldere recursiv
        all_files = find_all_files_recursively(folder_path)

        # Verifică dacă există fișiere în folder (poate fi gol)
        if not all_files:
            print(f"⚠️ Nu există fișiere în folderul '{folder_name}', se sare peste.")
            continue

        # Filtrează doar fișierele cu extensii acceptate
        relevant_files = [f for f in all_files
                         if os.path.splitext(f)[1].lower() in upload_exts]

        # Verifică dacă există fișiere relevante
        if not relevant_files:
            print(f"⚠️ Nu s-au găsit fișiere relevante în '{folder_name}', se sare peste.")
            continue

        # Prioritizează PDF-urile
        pdfs = [f for f in relevant_files if f.lower().endswith('.pdf')]

        # Organizăm fișierele pe subfoldere pentru a procesa fiecare titlu separat
        subfolders = {}

        # Dacă avem PDF-uri, le grupăm pe subdirectoare
        if pdfs:
            for pdf in pdfs:
                # Calea relativă față de folder_path
                rel_path = os.path.relpath(pdf, folder_path)
                parts = rel_path.split(os.sep)

                # Determinăm subfolderul (dacă există)
                if len(parts) > 1:
                    subfolder = parts[0]
                else:
                    subfolder = 'root'

                # Adăugăm la dicționar
                if subfolder not in subfolders:
                    subfolders[subfolder] = {'pdfs': [], 'other': []}

                subfolders[subfolder]['pdfs'].append(pdf)

            # Adăugăm restul fișierelor relevante la subdirectoarele corespunzătoare
            for file in relevant_files:
                if file in pdfs:
                    continue  # Sărim peste PDF-uri, deja procesate

                rel_path = os.path.relpath(file, folder_path)
                parts = rel_path.split(os.sep)

                if len(parts) > 1:
                    subfolder = parts[0]
                else:
                    subfolder = 'root'

                if subfolder not in subfolders:
                    subfolders[subfolder] = {'pdfs': [], 'other': []}

                subfolders[subfolder]['other'].append(file)
        else:
            # Nu avem PDF-uri, folosim fallback
            print(f"⚠️ Nu s-au găsit PDF-uri în '{folder_name}', folosim fallback.")

            # Grupăm fișierele pe subdirectoare pentru fallback
            for file in relevant_files:
                rel_path = os.path.relpath(file, folder_path)
                parts = rel_path.split(os.sep)

                if len(parts) > 1:
                    subfolder = parts[0]
                else:
                    subfolder = 'root'

                if subfolder not in subfolders:
                    subfolders[subfolder] = {'pdfs': [], 'other': []}

                subfolders[subfolder]['other'].append(file)

        # Procesăm fiecare subfolder
        if subfolders:
            print(f"📚 Găsite {len(subfolders)} titluri/subfoldere pentru '{folder_name}'")

            for subfolder, files in subfolders.items():
                pdfs = files['pdfs']
                other_files = files['other']

                # Dacă avem PDF-uri, facem upload la tot
                if pdfs:
                    # Folosim primul PDF pentru titlu
                    first_pdf = pdfs[0]
                    title = os.path.splitext(os.path.basename(first_pdf))[0]

                    # Curățăm titlul
                    if " - v." in title:
                        title = title.split(" - v.")[0]
                    elif " - ctrl" in title:
                        title = title.split(" - ctrl")[0]
                    elif " - scan" in title:
                        title = title.split(" - scan")[0]

                    # Combinăm toate fișierele
                    all_subfolder_files = pdfs + other_files

                    print(f"  📕 Procesez titlul: {title} ({len(all_subfolder_files)} fișiere, inclusiv {len(pdfs)} PDF-uri)")
                    upload_to_archive(all_subfolder_files, title)
                    time.sleep(4)  # Pauză între upload-uri
                else:
                    # Fără PDF-uri, facem fallback
                    if not other_files:
                        print(f"  ⚠️ Subfolderul '{subfolder}' nu conține fișiere relevante, se sare peste.")
                        continue

                    # Găsim un titlu din primul fișier
                    first_file = other_files[0]
                    title = os.path.splitext(os.path.basename(first_file))[0]

                    # Curățăm titlul
                    if " - v." in title:
                        title = title.split(" - v.")[0]
                    elif " - ctrl" in title:
                        title = title.split(" - ctrl")[0]
                    elif " - scan" in title:
                        title = title.split(" - scan")[0]

                    print(f"  📙 Fallback pentru titlul: {title} (fără PDF-uri, doar {len(other_files)} alte fișiere)")
                    fallback_copy(other_files, title)
                    time.sleep(1)  # Pauză scurtă între operații
        else:
            print(f"❌ Nu s-au găsit fișiere relevante organizate în subfoldere pentru '{folder_name}'")

    print("\n✅ Procesare completă!")

if __name__ == "__main__":
    try:
        process_all_folders()
    except KeyboardInterrupt:
        print("\n🛑 Script oprit manual de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare neașteptată: {e}")