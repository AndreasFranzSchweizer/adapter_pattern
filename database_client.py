from csv_importer import CSVImporter

class DataProvider:
    def read_data(self):
        pass

class DatabaseClient:
    def import_data(self, data_provider):
        data = data_provider.read_data()
        self.insert_into_database(data)

    def insert_into_database(self, data):
        print("Daten wurden in die Datenbank eingefügt:")
        print(data)


if __name__ == "__main__":
    csv_file_path = 'test_data.csv'  
    csv_importer = CSVImporter(csv_file_path)

    client = DatabaseClient()

    # hier benötigen wir einen Adapter
    client.import_data(csv_importer)
