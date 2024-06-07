import csv
from app.main.domain.entities.csv_data import Person
from app.main.domain.helpers.csv_file_path_helpers import CsvFilePathHelpers
from app.main.domain.helpers.csv_repository_helpers import CsvRepositoryHelpers

class CSVRepository:
    def read_data(self):
        with open(CsvFilePathHelpers.CSV_FILE_PATH, mode=CsvRepositoryHelpers.MODE) as file:
            csv_reader = csv.DictReader(file)
            persons = []
            for row in csv_reader:
                person = Person(
                    id=row[CsvRepositoryHelpers.ID],
                    name=row[CsvRepositoryHelpers.NAME],
                    age=row[CsvRepositoryHelpers.AGE]
                )
                persons.append(person)
            return persons

    def print_data(self, data):
        for person in data:
            print(f"ID: {person.id}, Name: {person.name}, Age: {person.age}")

