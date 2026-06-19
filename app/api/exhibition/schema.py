from apiflask import fields
from apiflask.schemas import Schema

class ArtPaletteSchema(Schema):
    red = fields.Integer(required=True)
    green = fields.Integer(required=True)
    blue = fields.Integer(required=True)

class ArtResponseSchema(Schema):
    title = fields.String(required=True)
    s3_key = fields.String(required=True)
    status = fields.String(required=True)
    palette = fields.Nested(ArtPaletteSchema, required=False)


class ExhibitionRequestSchema(Schema):
    exhibition_title = fields.String(required=True)

class ExhibitionResponseSchema(Schema):
    exhibition_id = fields.String(required=True)
    exhibition_title = fields.String(required=True)
    arts = fields.List(fields.Nested(ArtResponseSchema), required=True)
