import pandas as pd
import random
import os
from datetime import datetime, timedelta

def generate_random_name():
    """Generează un nume și prenume aleatoriu"""

    first_names = [
        "Alexandru", "Maria", "Andrei", "Elena", "Mihai", "Ana", "Cristian", "Ioana",
        "Gabriel", "Andreea", "Ionut", "Laura", "Florin", "Simona", "Daniel", "Alina",
        "George", "Raluca", "Bogdan", "Claudia"
    ]

    last_names = [
        "Popescu", "Ionescu", "Popa", "Constantin", "Stan", "Dumitru", "Gheorghe",
        "Stoica", "Matei", "Nicolae", "Vasile", "Dinu", "Mihai", "Georgescu", "Marin",
        "Tudor", "Dima", "Cristea", "Ciobanu", "Florea"
    ]

    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email(name):
    """Generează un email aleatoriu bazat pe nume"""

    # Simplificăm numele (eliminăm spații și diacritice)
    simplified_name = name.lower().replace(' ', '.').replace('ă', 'a').replace('â', 'a').replace('î', 'i').replace('ș', 's').replace('ț', 't')

    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "companie.ro", "firma.ro", "example.com"]

    return f"{simplified_name}@{random.choice(domains)}"

def generate_random_phone():
    """Generează un număr de telefon aleatoriu în format românesc"""

    prefixes = ["072", "073", "074", "075", "076", "077", "078", "079"]

    # Generăm restul cifrelor pentru număr
    suffix = ''.join([str(random.randint(0, 9)) for _ in range(7)])

    return f"{random.choice(prefixes)}{suffix}"

def generate_random_message():
    """Generează un mesaj aleatoriu"""

    messages = [
        "Doresc mai multe informații despre serviciile oferite.",
        "Sunt interesat de ofertele dumneavoastră. Vă rog să mă contactați.",
        "Aș dori să colaborăm pe un proiect viitor. Vă stau la dispoziție pentru detalii.",
        "Vă contactez referitor la posibilitățile de colaborare între companiile noastre.",
        "Am văzut portofoliul dumneavoastră și sunt impresionat. Aș dori să discutăm.",
        "Caut o soluție pentru problema mea și cred că serviciile dumneavoastră s-ar potrivi.",
        "Mă interesează o consultație referitoare la serviciile oferite.",
        "Aș dori un deviz pentru serviciile de consultanță menționate pe site.",
        "Vă contactez la recomandarea unui prieten. Aș dori mai multe detalii.",
        "Am o întrebare legată de serviciile dumneavoastră. Când aș putea primi un răspuns?",
        "Sunt în căutarea unui specialist în domeniu. Aș dori să știu disponibilitatea dumneavoastră.",
        "Vreau să vă mulțumesc pentru informațiile de pe site și aș dori să aflu mai multe detalii.",
        "Sunt interesat de o colaborare pe termen lung. Putem programa o discuție telefonică?",
        "Am nevoie de o ofertă personalizată pentru compania mea. Vă rog să mă contactați.",
        "Mă interesează să aflu mai multe despre metodologia dumneavoastră de lucru."
    ]

    return random.choice(messages)

def create_excel_data(filename, num_records=100):
    """
    Creează un fișier Excel cu date aleatorii pentru testarea formularelor

    Args:
        filename: Numele fișierului Excel care va fi creat
        num_records: Numărul de înregistrări care vor fi generate
    """

    # Lista categoriilor și subcategoriilor
    categorii = ["Personal", "Profesional", "Educație", "Altele"]
    subcategorii_per_categorie = {
        "Personal": ["Hobby", "Sănătate", "Familie", "Sport", "Călătorii"],
        "Profesional": ["Programare", "Design", "Marketing", "Vânzări", "Management"],
        "Educație": ["Cursuri", "Tutoriale", "Cărți", "Mentorat", "Certificări"],
        "Altele": ["Diverse", "Feedback", "Sugestii", "Reclamații", "Informații"]
    }

    # Generăm datele
    data = []

    for i in range(num_records):
        # Generăm un nume aleatoriu
        nume = generate_random_name()

        # Alegem o categorie aleatorie
        categorie = random.choice(categorii)

        # Alegem o subcategorie corespunzătoare categoriei
        subcategorie = random.choice(subcategorii_per_categorie[categorie])

        # Adăugăm înregistrarea la date
        data.append({
            'nume': nume,
            'email': generate_random_email(nume),
            'telefon': generate_random_phone(),
            'categorie': categorie,
            'subcategorie': subcategorie,
            'mesaj': generate_random_message(),
            'data_generare': (datetime.now() + timedelta(days=i % 30)).strftime("%Y-%m-%d")
        })

    # Creăm DataFrame-ul
    df = pd.DataFrame(data)

    # Salvăm datele în Excel
    df.to_excel(filename, index=False)

    print(f"Fișierul Excel '{filename}' a fost creat cu succes!")
    print(f"Conține {num_records} înregistrări aleatorii.")

    return df

if __name__ == "__main__":
    print("=== GENERARE DATE EXCEL PENTRU TESTARE FORMULARE ===")

    # Numele implicit al fișierului
    default_filename = "date_formulare.xlsx"

    # Solicităm numele fișierului (opțional)
    filename = input(f"Introduceți numele fișierului Excel (implicit: {default_filename}): ").strip()
    if not filename:
        filename = default_filename

    # Dacă nu are extensia .xlsx, o adăugăm
    if not filename.lower().endswith('.xlsx'):
        filename += '.xlsx'

    # Solicităm numărul de înregistrări
    num_records_str = input("Introduceți numărul de înregistrări (implicit: 100): ").strip()
    try:
        num_records = int(num_records_str) if num_records_str else 100
    except ValueError:
        print("Număr invalid. Se folosește valoarea implicită: 100")
        num_records = 100

    # Generăm fișierul Excel
    df = create_excel_data(filename, num_records)

    # Afișăm primele 5 înregistrări pentru vizualizare
    print("\nPrimele 5 înregistrări generate:")
    print(df.head().to_string())

    # Afișăm calea completă a fișierului
    abs_path = os.path.abspath(filename)
    print(f"\nFișierul a fost salvat la: {abs_path}")

    print("\nAceste date pot fi folosite pentru testarea automatizării formularelor.")