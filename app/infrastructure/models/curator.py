from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from app.domain.entities import Curator
from config import config


class CuratorModel(Model):
    class Meta:
        table_name = config.CURATOR_TABLE_NAME
        region = config.AWS_REGION

    curator_id = UnicodeAttribute(hash_key=True)
    curator_name = UnicodeAttribute(null=False)

    @classmethod
    def from_entity(cls, curator: Curator) -> "CuratorModel":
        return cls(curator_id=curator.curator_id, curator_name=curator.curator_name)
