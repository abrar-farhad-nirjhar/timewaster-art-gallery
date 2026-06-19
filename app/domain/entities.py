import uuid
from dataclasses import dataclass, field
from app.domain.value_objects import ArtPalette, ArtworkStatus


@dataclass
class Art:
    title: str
    s3_key: str
    status: ArtworkStatus = ArtworkStatus.PENDING
    palette: ArtPalette | None = None


@dataclass
class Exhibition:
    exhibition_title: str
    exhibition_id: uuid.UUID = field(default_factory=uuid.uuid4)
    arts: list[Art] = field(default_factory=list)


@dataclass
class CuratorExhibition:
    curator_id: uuid.UUID = field(default_factory=uuid.uuid4)
    exhibitions: list[Exhibition] = field(default_factory=list)
