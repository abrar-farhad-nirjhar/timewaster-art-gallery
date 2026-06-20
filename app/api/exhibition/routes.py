from app.api.blueprint import blueprint as bp
from app.api.exhibition.schema import ExhibitionRequestSchema, ExhibitionResponseSchema
from app.application.exhibition_service import ExhibitionService
from app.domain.entities import Exhibition


@bp.post("/curator/<curator_id>/exhibitions")
@bp.output(ExhibitionResponseSchema, status_code=201)
@bp.input(ExhibitionRequestSchema, location="json", arg_name="exhibition")
def create_exhibition(curator_id: str, exhibition: dict):
    service = ExhibitionService()
    exhibition = Exhibition.from_request(exhibition, curator_id)
    created_exhibition = service.create_exhibition(exhibition)
    return created_exhibition


@bp.get("/curator/<curator_id>/exhibitions")
@bp.output(ExhibitionResponseSchema(many=True), status_code=200)
def get_exhibitions(curator_id: str):
    service = ExhibitionService()
    return service.get_exhibitions(curator_id)


@bp.get("/curator/<curator_id>/exhibitions/<exhibition_id>")
@bp.output(ExhibitionResponseSchema, status_code=200)
def get_exhibition(curator_id: str, exhibition_id: str):
    service = ExhibitionService()
    return service.get_exhibition(curator_id, exhibition_id)


@bp.delete("/curator/<curator_id>/exhibitions/<exhibition_id>")
@bp.output(status_code=204)
def delete_exhibition(curator_id: str, exhibition_id: str):
    service = ExhibitionService()
    service.delete_exhibition(curator_id, exhibition_id)
