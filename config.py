import dataclasses
import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


@dataclasses.dataclass(frozen=True)
class Config:
    ARTWORK_TABLE_NAME: str
    CURATOR_TABLE_NAME: str
    EXHIBITION_TABLE_NAME: str
    AWS_REGION: str
    S3_BUCKET: str

    @classmethod
    def from_env(cls):
        return cls(
            ARTWORK_TABLE_NAME=os.environ.get("ARTWORK_TABLE_NAME", ""),
            CURATOR_TABLE_NAME=os.environ.get("CURATOR_TABLE_NAME", ""),
            EXHIBITION_TABLE_NAME=os.environ.get("EXHIBITION_TABLE_NAME", ""),
            AWS_REGION=os.environ.get("AWS_REGION", ""),
            S3_BUCKET=os.environ.get("S3_BUCKET", ""),
        )


config = Config.from_env()
