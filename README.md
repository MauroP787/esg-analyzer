# ESG Analyzer

Strumento per l'analisi automatizzata di bilanci di sostenibilità (PDF) di aziende quotate italiane, secondo gli standard ESRS.

## Stato del progetto
🚧 In sviluppo — Fase 1: estrazione testo da PDF

## Cosa fa finora
- Legge automaticamente tutti i PDF nella cartella `data/raw_pdfs/`
- Estrae il testo con `pdfplumber`
- Salva il testo estratto in `data/extracted_text/`

## Come si esegue
## Roadmap
- [x] Estrazione testo da PDF
- [ ] Pulizia e normalizzazione del testo
- [ ] Mapping alle categorie ESRS
- [ ] Analisi con AI
- [ ] Report strutturato