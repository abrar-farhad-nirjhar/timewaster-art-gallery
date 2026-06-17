from apiflask.schemas import Schema
from apiflask import fields



class HealthCheckResponseSchema(Schema):
    status = fields.String(required=True)
