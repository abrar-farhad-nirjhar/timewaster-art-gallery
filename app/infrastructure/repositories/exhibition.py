from app.domain.entities import Exhibition
from app.infrastructure.models.exhibition import ExhibitionModel


class ExhibitionRepository:
    def get_by_id(self, curator_id: str, exhibition_id: str) -> Exhibition:
        return Exhibition.from_model(
            ExhibitionModel.get(
                hash_key=exhibition_id,
                range_key=curator_id,
            )
        )

    def get_exhibitions_by_curator(self, curator_id: str) -> list[Exhibition]:
        return [
            Exhibition.from_model(exhibition_model)
            for exhibition_model in ExhibitionModel.curator_index.query(curator_id)
        ]

    def create_exhibition(self, exhibition: Exhibition) -> Exhibition:
        ExhibitionModel.from_entity(exhibition).save()
        return exhibition

    def update_exhibition(self, exhibition: Exhibition) -> Exhibition:
        exhibition_model = ExhibitionModel.get(exhibition.exhibition_id)
        exhibition_model.exhibition_name = exhibition.exhibition_name
        exhibition_model.exhibition_description = exhibition.exhibition_description
        exhibition_model.save()
        return exhibition

    def delete_exhibition(self, curator_id: str, exhibition_id: str) -> None:
        ExhibitionModel.get(exhibition_id, curator_id).delete
