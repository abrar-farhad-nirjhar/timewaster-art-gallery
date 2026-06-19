from app.api.blueprint import blueprint as bp
from app.application.exhibition_service import CuratorExhibitionService
from app.infrastructure.repositories.exhibition import CuratorExhibitionRepository
from app.domain.entities import CuratorExhibition
from app.api.curator.schema import CuratorResponseSchema



@bp.post("/curators")
@bp.output(CuratorResponseSchema, status_code=201)
def create_curator_exhibition():
    repo = CuratorExhibitionRepository()
    service = CuratorExhibitionService(repo)
    curator_exhibition = CuratorExhibition()
    created_curator_exhibition = service.create_curator_exhibition(curator_exhibition)
    return created_curator_exhibition