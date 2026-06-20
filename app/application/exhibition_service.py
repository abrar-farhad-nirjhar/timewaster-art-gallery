from app.domain.entities import Exhibition
from app.infrastructure.repositories.exhibition import ExhibitionRepository


class ExhibitionService:
    def __init__(self):
        self.repo = ExhibitionRepository()

    def get_exhibition(self, curator_id: str, exhibition_id: str) -> Exhibition:
        return self.repo.get_by_id(curator_id, exhibition_id)

    def get_exhibitions(self, curator_id: str) -> list[Exhibition]:
        return self.repo.get_exhibitions_by_curator(curator_id)

    def create_exhibition(self, exhibition: Exhibition) -> Exhibition:
        return self.repo.create_exhibition(exhibition)

    def delete_exhibition(self, curator_id: str, exhibition_id: str) -> None:
        self.repo.delete_exhibition(curator_id, exhibition_id)
