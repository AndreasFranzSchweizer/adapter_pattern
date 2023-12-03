import csv

class CSVImporter:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self):
        data = []
        try:
            with open(self.file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Die Datei '{self.file_path}' wurde nicht gefunden.")
        except Exception as e:
            print(f"Fehler beim Lesen der CSV-Datei: {e}")

        return data
