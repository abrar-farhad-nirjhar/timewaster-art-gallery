from app.api.blueprint import blueprint as bp
from app.application.exhibition_service import CuratorExhibitionService
from app.infrastructure.repositories.exhibition import CuratorExhibitionRepository
from app.domain.entities import Exhibition
from app.api.exhibition.schema import ExhibitionResponseSchema, ExhibitionRequestSchema, ExhibitionResponseSchema


@bp.post("/curator/<curator_id>/exhibitions")
@bp.output(ExhibitionResponseSchema, status_code=201)
@bp.input(ExhibitionRequestSchema, location="json", arg_name="body")
def create_exhibition(curator_id: str, body: dict):
    repo = CuratorExhibitionRepository()
    service = CuratorExhibitionService(repo)
    exhibition = Exhibition(exhibition_title=body["exhibition_title"])
    created_exhibition = service.create_exhibition(curator_id, exhibition)
    return created_exhibition



@bp.get("/curator/<curator_id>/exhibitions")
@bp.output(ExhibitionResponseSchema(many=True), status_code=200)
def get_exhibitions(curator_id: str):
    repo = CuratorExhibitionRepository()
    service = CuratorExhibitionService(repo)
    curator_exhibition = service.repo.get_by_curator_id(curator_id)
    return curator_exhibition.exhibitions


