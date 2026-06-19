from apiflask.schemas import Schema
from apiflask import fields
from app.api.exhibition.schema import ExhibitionResponseSchema


class CuratorResponseSchema(Schema):
    curator_id = fields.String(required=True)
    exhibitions = fields.List(fields.Nested(ExhibitionResponseSchema), required=True)
