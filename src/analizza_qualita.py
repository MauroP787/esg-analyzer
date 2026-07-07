from collections import Counter

def trova_righe_ripetute(percorso_file, soglia=10):
    with open(percorso_file, "r", encoding="utf-8") as f:
        righe = f.readlines()

    righe_pulite = [riga.strip() for riga in righe if riga.strip()]

    conteggio = Counter(righe_pulite)

    print(f"\n--- {percorso_file} ---")
    print(f"Righe totali (non vuote): {len(righe_pulite)}")
    print(f"Righe distinte: {len(conteggio)}")
    print(f"\nRighe che si ripetono più di {soglia} volte (probabile rumore):\n")

    for riga, volte in conteggio.most_common(40):
        if volte > soglia and len(riga) > 15:
            print(f"  [{volte}x] {riga[:80]}")
def pulisci_testo(percorso_input, percorso_output, soglia=10):
    with open(percorso_input, "r", encoding="utf-8") as f:
        righe = f.readlines()

    righe_pulite = [riga.strip() for riga in righe if riga.strip()]
    conteggio = Counter(righe_pulite)

    righe_da_rimuovere = {riga for riga, volte in conteggio.items() if volte > soglia}

    righe_finali = [riga for riga in righe_pulite if riga not in righe_da_rimuovere]

    with open(percorso_output, "w", encoding="utf-8") as f:
        f.write("\n".join(righe_finali))

    print(f"{percorso_input}: {len(righe_pulite)} righe -> {len(righe_finali)} righe pulite")
    print(f"  Rimosse {len(righe_da_rimuovere)} righe distinte ripetute troppo spesso")

if __name__ == "__main__":
    pulisci_testo("data/extracted_text/ferrari_report_2025.txt", "data/extracted_text/ferrari_report_2025_pulito.txt")
    pulisci_testo("data/extracted_text/terna_report_2025.txt", "data/extracted_text/terna_report_2025_pulito.txt")
    pulisci_testo("data/extracted_text/eni_report_2025.txt", "data/extracted_text/eni_report_2025_pulito.txt")
    