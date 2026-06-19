from app.domain.entities import CuratorExhibition, Exhibition
from app.infrastructure.repositories.exhibition import CuratorExhibitionRepository


class CuratorExhibitionService:
    def __init__(self, repo: CuratorExhibitionRepository):
        self.repo = repo
    
    def create_curator_exhibition(
            self, curator_exhibition: CuratorExhibition) -> CuratorExhibition:
        self.repo.save(curator_exhibition)
        return curator_exhibition
    
    def create_exhibition(self, curator_id: str, exhibition: Exhibition) -> Exhibition:
        curator_exhibition = self.repo.get_by_curator_id(curator_id)
        curator_exhibition.exhibitions.append(exhibition)
        self.repo.save(curator_exhibition)
        return exhibition