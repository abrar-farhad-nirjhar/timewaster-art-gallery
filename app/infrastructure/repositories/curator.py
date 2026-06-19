from app.domain.entities import Curator
from app.infrastructure.models.curator import CuratorModel


class CuratorRepository:
    def get_curators(self) -> list[Curator]:
        curators = []
        for curator_model in CuratorModel.scan():
            curators.append(Curator.from_model(curator_model))
        return curators

    def get_by_id(self, curator_id: str) -> Curator:
        return Curator.from_model(CuratorModel.get(curator_id))

    def create_curator(self, curator: Curator) -> Curator:
        CuratorModel.from_entity(curator).save()
        return curator

    def update_curator(self, curator: Curator) -> Curator:
        curator_model = CuratorModel.get(curator.curator_id)
        curator_model.curator_name = curator.curator_name
        curator_model.save()
        return Curator

    def delete_curator(self, curator_id: str) -> None:
        CuratorModel.get(curator_id).delete()
