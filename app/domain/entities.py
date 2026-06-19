import uuid
from dataclasses import dataclass, field

from app.domain.value_objects import ArtWorkPalette, ArtworkStatus
from app.infrastructure.models.artwork import ArtWorkModel
from app.infrastructure.models.curator import CuratorModel
from app.infrastructure.models.exhibition import ExhibitionModel


@dataclass
class Curator:
    curator_id = field(default_factory=uuid.uuid4)
    curator_name: str

    @classmethod
    def from_model(cls, model: CuratorModel) -> "Curator":
        return cls(
            curator_id=model.curator_id,
            curator_name=model.curator_name,
        )


@dataclass
class Exhibition:
    exhibition_id = field(default_factory=uuid.uuid4)
    curator_id: uuid.UUID
    exhibition_name: str
    exhibition_description: str | None

    @classmethod
    def from_model(cls, model: ExhibitionModel) -> "Exhibition":
        return cls(
            exhibition_id=model.exhibtion_id,
            curator_id=model.curator_id,
            exhibition_name=model.exhibition_name,
            exhibition_description=model.exhibition_description,
        )


@dataclass
class ArtWork:
    artwork_id = field(default_factory=uuid.uuid4)
    owner: str
    title: str
    s3_key: str | None
    status: ArtworkStatus
    palette: ArtWorkPalette

    @classmethod
    def from_model(cls, model: ArtWorkModel) -> "ArtWork":
        return cls(
            artwork_id=model.artwork_id,
            owner=model.owner,
            title=model.title,
            s3_key=model.s3_key,
            status=ArtworkStatus(model.status),
            palette=ArtWorkPalette(
                red=model.palette.red,
                green=model.palette.green,
                blue=model.palette.blue,
            ),
        )
