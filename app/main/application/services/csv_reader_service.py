from app.main.infrastructure.repositories.csv_repository import CSVRepository
from app.main.application.interfaces.csv_reader_service_interface import CSVReaderServiceInterface

class CSVReaderService(CSVReaderServiceInterface):
    def __init__(self, csv_repository: CSVRepository):
        self.csv_repository = csv_repository

    def read_data(self):
        return self.csv_repository.read_data()

    def print_data(self, data):
        self.csv_repository.print_data(data)
