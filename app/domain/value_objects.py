from enum import Enum
from dataclasses import dataclass


class ArtworkStatus(Enum):
    PENDING = "pending"
    CURATED = "curated"


@dataclass(frozen=True)
class ArtWorkPalette:
    red: int
    green: int
    blue: int