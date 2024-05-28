from typing import List
from app.main.domain.entities import DataRecord
from app.main.application.interfaces.mapper_config_repository import IDataRepository

class CSVService:
    def __init__(self, repository: IDataRepository):
        self.repository = repository

    def get_data(self) -> List[DataRecord]:
        return self.repository.read_data()
