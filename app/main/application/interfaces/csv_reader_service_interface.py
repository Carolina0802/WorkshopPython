from abc import ABC, abstractmethod

class CSVReaderServiceInterface(ABC):
    @abstractmethod
    def read_data(self):
        pass
