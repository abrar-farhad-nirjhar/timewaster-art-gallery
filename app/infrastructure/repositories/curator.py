from app.domain.entities import Curator
from app.helpers.translators import Translator
from app.infrastructure.models.curator import CuratorModel


class CuratorRepository:
    def __init__(self) -> None:
        self.translator = Translator.get_translator(CuratorModel)

    def get_curators(self) -> list[Curator]:
        curators = []
        for curator_model in CuratorModel.scan():
            curators.append(self.translator.model_to_entity(curator_model))
        return curators

    def get_by_id(self, curator_id: str) -> Curator:
        return self.translator.model_to_entity(CuratorModel.get(curator_id))

    def create_curator(self, curator: Curator) -> Curator:
        self.translator.entity_to_model(curator).save()
        return curator

    def update_curator(self, curator: Curator) -> Curator:
        curator_model = CuratorModel.get(curator.curator_id)
        curator_model.curator_name = curator.curator_name
        curator_model.save()
        return Curator

    def delete_curator(self, curator_id: str) -> None:
        CuratorModel.get(curator_id).delete()
