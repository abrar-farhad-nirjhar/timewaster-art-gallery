from app.domain.entities import ArtWork
from app.infrastructure.models.artwork import ArtWorkModel, construct_owner


class ArtWorkRepository:
    def get_by_id(
        self,
        curator_id: str,
        exhibition_id: str,
        artwork_id: str,
    ) -> ArtWork:
        owner = construct_owner(curator_id, exhibition_id)
        return ArtWork.from_model(ArtWorkModel.get(artwork_id, owner))

    def get_by_owner(
        self,
        curator_id: str,
        exhibition_id: str,
    ) -> list[ArtWork]:
        owner = construct_owner(curator_id, exhibition_id)
        return [
            ArtWork.from_model(artwork_model)
            for artwork_model in ArtWorkModel.owner_index.query(owner)
        ]
