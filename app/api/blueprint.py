from apiflask.blueprint import APIBlueprint


blueprint = APIBlueprint("api", __name__, url_prefix="/api")

from app.api.health import routes as health_routes
from app.api.exhibition import routes as exhibition_routes
from app.api.curator import routes as curator_routes