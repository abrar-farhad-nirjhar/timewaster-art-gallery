import os
import dataclasses
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


@dataclasses.dataclass(frozen=True)
class Config:
    DDB_NAME: str
    AWS_REGION: str
    S3_BUCKET: str

    @classmethod
    def from_env(cls):
        return cls(
            DDB_NAME=os.environ.get("DDB_NAME", ""),
            AWS_REGION=os.environ.get("AWS_REGION", ""),
            S3_BUCKET=os.environ.get("S3_BUCKET", "")
        )

config = Config.from_env()