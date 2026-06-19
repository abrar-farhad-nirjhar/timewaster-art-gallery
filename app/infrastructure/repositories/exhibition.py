from app.infrastructure.models.exhibition import CuratorExhibitionModel, ExhibitionModel, ArtModel, ArtColorPaletteModel
from app.domain.entities import CuratorExhibition, Exhibition, Art, ArtPalette
from app.domain.value_objects import ArtPalette, ArtworkStatus

class CuratorExhibitionRepository:
    def get_exhibition_by_id(self, curator_id: str, exhibition_id: str) -> Exhibition:
        curator_exhibition_model = CuratorExhibitionModel.get(curator_id)
        exhibition_model = next(
            (exhibition for exhibition in curator_exhibition_model.exhibitions if exhibition.exhibition_id == exhibition_id),
            None
        )
        if not exhibition_model:
            raise ValueError(f"Exhibition with ID {exhibition_id} not found for curator {curator_id}")

        arts = [
            Art(
                title=art_model.title,
                s3_key=art_model.s3_key,
                status=ArtworkStatus(art_model.status),
                palette=ArtPalette(
                    art_model.palette.red,
                    art_model.palette.green,
                    art_model.palette.blue) if art_model.palette else None,
            )
            for art_model in exhibition_model.arts
        ]

        return Exhibition(
            exhibition_title=exhibition_model.exhibition_title,
            exhibition_id=exhibition_model.exhibition_id,
            arts=arts
        )

    def get_by_curator_id(self, curator_id: str) -> CuratorExhibition:
        curator_exhibition_model = CuratorExhibitionModel.get(curator_id)
        exhibitions = [
            Exhibition(
                exhibition_title=exhibition_model.exhibition_title,
                exhibition_id=exhibition_model.exhibition_id,
                arts=[
                    Art(
                        title=art_model.title,
                        s3_key=art_model.s3_key,
                        status=ArtworkStatus(art_model.status),
                        palette=ArtPalette(
                            art_model.palette.red,
                            art_model.palette.green,
                            art_model.palette.blue) if art_model.palette else None,
                    )
                    for art_model in exhibition_model.arts
                ],
            )
            for exhibition_model in curator_exhibition_model.exhibitions
        ]
        return CuratorExhibition(
            curator_id=curator_exhibition_model.curator_id,
            exhibitions=exhibitions,
        )
    def save(self, curator_exhibition: CuratorExhibition):
        curator_exhibition_model = CuratorExhibitionModel(
            curator_id=str(curator_exhibition.curator_id),
            exhibitions=[
                ExhibitionModel(
                    exhibition_title=exhibition.exhibition_title,
                    exhibition_id=str(exhibition.exhibition_id),
                    arts=[
                        ArtModel(
                            title=art.title,
                            s3_key=art.s3_key,
                            status=art.status.value,
                            palette=ArtColorPaletteModel(
                                red=art.palette.red,
                                green=art.palette.green,
                                blue=art.palette.blue) if art.palette else None,
                        )
                        for art in exhibition.arts
                    ],
                )
                for exhibition in curator_exhibition.exhibitions
            ],
        )
        curator_exhibition_model.save()