# Manuale per Script di Conversione HTML-CVS

Questo script è stato creato per convertire tutti i file HTML presenti in una directory specificata in un singolo file CSV. Di seguito è spiegato come funziona lo script e come utilizzarlo.

## Requisiti:
- Python 3.x
- Libreria BeautifulSoup4

## Installazione dei Requisiti:
Per installare BeautifulSoup4, esegui il seguente comando:

```bash
pip install beautifulsoup4


Descrizione dello Script:
Lo script contiene tre funzioni principali e un blocco di codice che viene eseguito quando lo script viene avviato.

get_all_htm_files(directory):

Questa funzione accetta come argomento il percorso della directory e restituisce una lista di tutti i file HTML presenti in quella directory.
extract_text_from_htm(file_name):

Questa funzione accetta come argomento il nome di un file HTML e restituisce una stringa contenente tutto il testo estratto dal file HTML.
convert_htm_files_to_csv(directory, output_file):

Questa funzione accetta come argomenti il percorso della directory e il nome del file CSV di output. Converte tutti i file HTML nella directory specificata in un singolo file CSV.
Utilizzo dello Script:
Assicurati che tutti i file HTML che desideri convertire siano presenti nella directory desiderata.
Modifica le seguenti righe di codice con il percorso della directory e il nome del file CSV di output desiderati:
python
Copy code
directory = "c:\\temp"  # Modifica questo con il percorso della tua directory
output_csv_file = os.path.join(directory, "output.csv")  # Modifica questo con il nome del file CSV di output desiderato
Esegui lo script da linea di comando o da un IDE Python. Durante l'esecuzione, lo script fornirà un feedback sui file convertiti con successo e su eventuali errori riscontrati.

Note:
Lo script utilizza la codifica 'utf-8-sig' per la lettura dei file HTML per gestire l'ordine dei byte (BOM) e 'utf-8' per la scrittura del file CSV per scrivere senza il BOM.
Il testo estratto dai file HTML viene sanificato rimuovendo virgole e tabulazioni per evitare problemi nel file CSV di output.

Contatto:
Per qualsiasi domanda o assistenza, contattare Mohammad Yaghuby.
