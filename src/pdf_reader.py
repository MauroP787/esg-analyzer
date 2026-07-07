import pdfplumber
import os

def estrai_testo_pdf(percorso_file):
    testo_completo = ""
    with pdfplumber.open(percorso_file) as pdf:
        for pagina in pdf.pages:
            testo = pagina.extract_text()
            if testo:
                testo_completo += testo + "\n"
    return testo_completo

if __name__ == "__main__":
    cartella_input = "data/raw_pdfs"
    cartella_output = "data/extracted_text"

    elenco_file = os.listdir(cartella_input)

    for nome_file in elenco_file:
        if nome_file.endswith(".pdf"):
            percorso_pdf = os.path.join(cartella_input, nome_file)

            print(f"Elaborazione di: {nome_file}...")
            testo = estrai_testo_pdf(percorso_pdf)

            nome_base = nome_file.replace(".pdf", "")
            percorso_output = os.path.join(cartella_output, nome_base + ".txt")

            with open(percorso_output, "w", encoding="utf-8") as f:
                f.write(testo)

            print(f"  -> {len(testo)} caratteri salvati in {percorso_output}")