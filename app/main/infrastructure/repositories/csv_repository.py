# app/main/infrastructure/repository/csv_repository.py
import csv
from app.main.domain.entities.csv_data import Person
from app.main.domain.helpers.csv_file_path import CSV_FILE_PATH

class CSVRepository:
    def read_data(self):
        with open(CSV_FILE_PATH, mode='r') as file:
            csv_reader = csv.DictReader(file)
            persons = []
            for row in csv_reader:
                person = Person()
                person.id = row['id']
                person.name = row['name']
                person.age = row['age']
                persons.append(person)
            return persons

    def print_data(self, data):
        for person in data:
            print(f"ID: {person.id}, Name: {person.name}, Age: {person.age}")
