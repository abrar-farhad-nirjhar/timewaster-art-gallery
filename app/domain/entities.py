import uuid
from dataclasses import dataclass, field

from app.domain.value_objects import ArtWorkPalette, ArtworkStatus


@dataclass
class Curator:
    curator_name: str
    curator_id: uuid.UUID = field(default_factory=uuid.uuid4)

    @classmethod
    def from_request(cls, curator: dict) -> "Curator":
        return cls(curator_name=curator["curator_name"])


@dataclass
class Exhibition:
    curator_id: uuid.UUID
    exhibition_name: str
    exhibition_description: str | None
    exhibition_id: uuid.UUID = field(default_factory=uuid.uuid4)

    @classmethod
    def from_request(cls, exhibition: dict, curator_id: str) -> "Exhibition":
        return cls(
            curator_id=curator_id,
            exhibition_name=exhibition["exhibition_name"],
            exhibition_description=exhibition.get("exhibition_description"),
        )


@dataclass
class ArtWork:
    owner: str
    title: str
    s3_key: str | None
    status: ArtworkStatus
    palette: ArtWorkPalette
    artwork_id: uuid.UUID = field(default_factory=uuid.uuid4)
