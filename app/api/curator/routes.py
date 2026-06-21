from apiflask.schemas import EmptySchema

from app.api.blueprint import blueprint as bp
from app.api.curator.schema import CuratorRequestSchema, CuratorResponseSchema
from app.application.curator_service import CuratorService
from app.domain.entities import Curator


@bp.post("/curator")
@bp.input(CuratorRequestSchema, location="json", arg_name="curator")
@bp.output(CuratorResponseSchema, status_code=201)
def create_curator(curator: dict):
    entity = Curator.from_request(curator)
    service = CuratorService()
    return service.create_curator(entity)


@bp.get("/curator")
@bp.output(CuratorResponseSchema(many=True), status_code=200)
def get_curators():
    service = CuratorService()
    return service.get_curators()


@bp.get("/curator/<curator_id>")
@bp.output(CuratorResponseSchema, status_code=200)
def get_curator(curator_id: str):
    service = CuratorService()
    return service.get_curator(curator_id)


@bp.delete("/curator/<curator_id>")
@bp.output(EmptySchema, status_code=204)
def delete_curator(curator_id: str):
    service = CuratorService()
    service.delete_curator(curator_id)
