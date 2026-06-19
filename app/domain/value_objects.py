from enum import Enum
from dataclasses import dataclass


class ArtworkStatus(Enum):
    PENDING = "pending"
    CURATED = "curated"


@dataclass(frozen=True)
class ArtPalette:
    red: int
    green: int
    blue: int