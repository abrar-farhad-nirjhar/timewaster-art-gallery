from app.domain.entities import ArtWork
from app.helpers.translators import Translator
from app.infrastructure.models.artwork import ArtWorkModel, construct_owner


class ArtWorkRepository:

    def __init__(self) -> None:
        self.translator = Translator.get_translator(ArtWorkModel)

    def get_by_id(
        self,
        curator_id: str,
        exhibition_id: str,
        artwork_id: str,
    ) -> ArtWork:
        owner = construct_owner(curator_id, exhibition_id)
        return self.translator.model_to_entity(ArtWorkModel.get(artwork_id, owner))

    def get_by_owner(
        self,
        curator_id: str,
        exhibition_id: str,
    ) -> list[ArtWork]:
        owner = construct_owner(curator_id, exhibition_id)
        return [
            self.translator.model_to_entity(artwork_model)
            for artwork_model in ArtWorkModel.owner_index.query(owner)
        ]
