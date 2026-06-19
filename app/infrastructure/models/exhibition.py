from pynamodb.models import Model
import pynamodb.attributes
from app.domain.entities import Art
from config import config
from app.domain.value_objects import ArtworkStatus


class ArtColorPaletteModel(pynamodb.attributes.MapAttribute):
    red = pynamodb.attributes.NumberAttribute()
    green = pynamodb.attributes.NumberAttribute()
    blue = pynamodb.attributes.NumberAttribute()


class ArtModel(pynamodb.attributes.MapAttribute):
    title = pynamodb.attributes.UnicodeAttribute()
    s3_key = pynamodb.attributes.UnicodeAttribute()
    status = pynamodb.attributes.UnicodeAttribute(default=ArtworkStatus.PENDING.value)
    palette = ArtColorPaletteModel()


class ExhibitionModel(pynamodb.attributes.MapAttribute):
    exhibition_id = pynamodb.attributes.UnicodeAttribute()
    exhibition_title = pynamodb.attributes.UnicodeAttribute()
    arts = pynamodb.attributes.ListAttribute(of=ArtModel, default=list)


class CuratorExhibitionModel(Model):
    class Meta:
        table_name = config.DDB_NAME
        region = config.DDB_REGION

    curator_id = pynamodb.attributes.UnicodeAttribute(hash_key=True)
    exhibitions = pynamodb.attributes.ListAttribute(of=ExhibitionModel, default=list)