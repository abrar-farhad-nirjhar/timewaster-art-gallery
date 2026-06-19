from pynamodb.attributes import UnicodeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model

from app.domain.entities import Exhibition
from config import config


class CuratorGSI(GlobalSecondaryIndex):
    class Meta:
        index_name = "curator-index"
        projection = AllProjection()

    curator_id = UnicodeAttribute(hash_key=True)


class ExhibitionModel(Model):
    class Meta:
        table_name = config.EXHIBITION_TABLE_NAME
        region = config.AWS_REGION

    exhibtion_id = UnicodeAttribute(hash_key=True)
    curator_id = UnicodeAttribute(range_key=True)
    exhibition_name = UnicodeAttribute(null=False)
    exhibition_description = UnicodeAttribute(null=True)

    curator_index = CuratorGSI()

    @classmethod
    def from_entity(cls, exhibition: Exhibition) -> "ExhibitionModel":
        return cls(
            exhibition_id=exhibition.exhibition_id,
            curator_id=exhibition.curator_id,
            exhibition_name=exhibition.exhibition_name,
            exhibition_description=exhibition.exhibition_description,
        )
