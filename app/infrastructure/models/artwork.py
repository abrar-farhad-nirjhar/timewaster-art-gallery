from pynamodb.attributes import MapAttribute, NumberAttribute, UnicodeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model

from config import config


def construct_owner(curator_id: str, exhibition_id: str) -> str:
    return f"{curator_id}#{exhibition_id}"


class ArtColorPaletteModel(MapAttribute):
    red = NumberAttribute()
    green = NumberAttribute()
    blue = NumberAttribute()


class OwnerGSI(GlobalSecondaryIndex):
    class Meta:
        index_name = "exhibition-index"
        projection = AllProjection()

    owner = UnicodeAttribute(hash_key=True)


class ArtWorkModel(Model):
    class Meta:
        table_name = config.ARTWORK_TABLE_NAME
        region = config.AWS_REGION

    artwork_id = UnicodeAttribute(hash_key=True)
    owner = UnicodeAttribute(range_key=True)
    title = UnicodeAttribute()
    s3_key = UnicodeAttribute()
    status = UnicodeAttribute()
    palette = ArtColorPaletteModel()

    owner_index = OwnerGSI()
