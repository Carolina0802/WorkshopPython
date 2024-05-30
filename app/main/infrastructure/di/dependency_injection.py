from app.main.application.services.csv_reader_service import CSVReaderService
from app.main.infrastructure.repositories.csv_repository import CSVRepository

def inject_dependencies():
    csv_repository = CSVRepository()
    csv_reader_service = CSVReaderService(csv_repository)
    return csv_reader_service
