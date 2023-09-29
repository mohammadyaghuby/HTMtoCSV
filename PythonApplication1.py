import os
import codecs
from bs4 import BeautifulSoup

def get_all_htm_files(directory):
    """Retrieve all .htm files from a specified directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.htm')]

def extract_text_from_htm(file_name):
    """Extract text from the specified .htm file."""
    with codecs.open(file_name, "r", "utf-8-sig") as f:  # Using 'utf-8-sig' to handle the BOM during reading
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    
    # Extracting all text and joining without any separator
    text_data = soup.get_text().splitlines()
    combined_text = ''.join([line.strip() for line in text_data if line.strip()])
    # Remove commas and tabs to ensure they don't create new columns or issues
    sanitized_text = combined_text.replace(',', '').replace('\t', ' ')
    return sanitized_text

def convert_htm_files_to_csv(directory, output_file):
    """Convert all .htm files in the specified directory to a single CSV file."""
    htm_files = get_all_htm_files(directory)
    
    with codecs.open(output_file, "w", "utf-8") as csv_file:  # Using 'utf-8' to write without the BOM
        for file_name in htm_files:
            try:
                line_data = extract_text_from_htm(file_name)
                csv_file.write(line_data + "\n")
                print(f"File {file_name} convertito con successo!")
            except Exception as e:
                print(f"Errore durante la conversione del file {file_name}: {e}")

if __name__ == "__main__":
    directory = "c:\\temp"
    output_csv_file = os.path.join(directory, "output.csv")
    convert_htm_files_to_csv(directory, output_csv_file)
