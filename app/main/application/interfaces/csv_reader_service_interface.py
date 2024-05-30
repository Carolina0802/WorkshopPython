# app/main/application/interfaces/csv_reader_service_interface.py
from abc import ABC, abstractmethod

class CSVReaderServiceInterface(ABC):
    @abstractmethod
    def read_data(self):
        pass
