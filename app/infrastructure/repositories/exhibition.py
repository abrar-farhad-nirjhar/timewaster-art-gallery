from app.domain.entities import Exhibition
from app.helpers.translators import Translator
from app.infrastructure.models.exhibition import ExhibitionModel


class ExhibitionRepository:
    def __init__(self) -> None:
        self.translator = Translator.get_translator(ExhibitionModel)

    def get_by_id(self, curator_id: str, exhibition_id: str) -> Exhibition:
        return self.translator.model_to_entity(
            ExhibitionModel.get(
                hash_key=exhibition_id,
                range_key=curator_id,
            )
        )

    def get_exhibitions_by_curator(self, curator_id: str) -> list[Exhibition]:
        return [
            self.translator.model_to_entity(exhibition_model)
            for exhibition_model in ExhibitionModel.curator_index.query(curator_id)
        ]

    def create_exhibition(self, exhibition: Exhibition) -> Exhibition:
        self.translator.entity_to_model(exhibition).save()
        return exhibition

    def update_exhibition(self, exhibition: Exhibition) -> Exhibition:
        exhibition_model = ExhibitionModel.get(exhibition.exhibition_id)
        exhibition_model.exhibition_name = exhibition.exhibition_name
        exhibition_model.exhibition_description = exhibition.exhibition_description
        exhibition_model.save()
        return exhibition

    def delete_exhibition(self, curator_id: str, exhibition_id: str) -> None:
        ExhibitionModel.get(exhibition_id, curator_id).delete
