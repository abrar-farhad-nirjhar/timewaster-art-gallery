from apiflask import fields
from apiflask.schemas import Schema


class ExhibitionRequestSchema(Schema):
    exhibition_name = fields.String(required=True, data_key="exhibition-name")
    exhibition_description = fields.String(
        required=False, data_key="exhibition-description"
    )


class ExhibitionResponseSchema(Schema):
    exhibition_id = fields.UUID(required=True, data_key="exhibition-id", dump_only=True)
    curator_id = fields.UUID(required=True, data_key="curator-id", dump_only=True)
    exhibition_name = fields.String(
        required=True, data_key="exhibition-name", dump_only=True
    )
    exhibition_description = fields.String(
        required=False, data_key="exhibition-description", dump_only=True
    )
