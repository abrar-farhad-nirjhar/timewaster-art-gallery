from app.infrastructure.repositories.artwork import ArtWorkRepository


class ArtWorkService:
    def __init__(self):
        self.repo = ArtWorkRepository()
