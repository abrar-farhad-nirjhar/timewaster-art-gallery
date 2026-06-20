from apiflask import fields
from apiflask.schemas import Schema


class CuratorRequestSchema(Schema):
    curator_name = fields.String(data_key="curator-name", required=True)


class CuratorResponseSchema(Schema):
    curator_id = fields.UUID(data_key="curator-id", required=True, dump_only=True)
    curator_name = fields.UUID(data_key="curator-name", required=True, dump_only=True)
