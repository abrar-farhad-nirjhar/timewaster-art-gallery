from app.api.blueprint import blueprint as bp
from app.api.health.schema import HealthCheckResponseSchema


@bp.get("/health")
@bp.output(HealthCheckResponseSchema, status_code=200)
def health_check():
    return {
        "status": "ok"
    }
