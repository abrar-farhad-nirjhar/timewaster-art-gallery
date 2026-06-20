from app.domain.entities import Curator
from app.infrastructure.repositories.curator import CuratorRepository


class CuratorService:
    def __init__(self):
        self.repo = CuratorRepository()

    def get_curator(self, curator_id: str) -> Curator:
        return self.repo.get_by_id(curator_id)

    def get_curators(self) -> list[Curator]:
        return self.repo.get_curators()

    def create_curator(self, curator: Curator) -> Curator:
        return self.repo.create_curator(curator)

    def delete_curator(self, curator_id: str) -> None:
        self.repo.delete_curator(curator_id)
