import os
import dataclasses
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


@dataclasses.dataclass(frozen=True)
class Config:
    DDB_NAME: str
    DDB_REGION: str

    @classmethod
    def from_env(cls):
        return cls(
            DDB_NAME=os.environ.get("DDB_NAME", ""),
            DDB_REGION=os.environ.get("DDB_REGION", ""),
        )

config = Config.from_env()