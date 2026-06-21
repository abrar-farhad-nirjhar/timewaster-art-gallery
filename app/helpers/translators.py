import abc
from typing import Generic, TypeVar

import pynamodb.models

import app.domain.entities as domain
import app.infrastructure.models as models

ModelType = TypeVar("ModelType", bound=pynamodb.models.Model)
EntityType = TypeVar("EntityType")


class Translator(abc.ABC, Generic[ModelType, EntityType]):
    _REGISTRY: dict[ModelType, type["Translator"]] = {}

    @abc.abstractmethod
    def model_to_entity(self, model: ModelType) -> EntityType:
        pass

    @abc.abstractmethod
    def entity_to_model(self, entity: EntityType) -> ModelType:
        pass

    @classmethod
    def register_translator(cls, model_cls: ModelType):
        def decorator(translator_cls: type[Translator[ModelType, EntityType]]):
            cls._REGISTRY[model_cls] = translator_cls
            return translator_cls

        return decorator

    @classmethod
    def get_translator(cls, model_cls: ModelType) -> "Translator":
        return cls.__REGISTRY[model_cls]


@Translator.register_translator(models.CuratorModel)
class CuratorTranslator(Translator[models.CuratorModel, domain.Curator]):
    def model_to_entity(self, model: models.CuratorModel) -> domain.Curator:
        return domain.Curator(
            curator_id=model.curator_id,
            curator_name=model.curator_name,
        )

    def entity_to_model(self, entity: domain.Curator) -> models.CuratorModel:
        return models.CuratorModel(
            curator_id=entity.curator_id,
            curator_name=entity.curator_name,
        )


@Translator.register_translator(models.ExhibitionModel)
class ExhibitionTranslator(Translator[models.ExhibitionModel, domain.Exhibition]):
    def model_to_entity(self, model: models.ExhibitionModel) -> domain.Exhibition:
        return domain.Exhibition(
            exhibition_id=model.exhibtion_id,
            curator_id=model.curator_id,
            exhibition_name=model.exhibition_name,
            exhibition_description=model.exhibition_description,
        )

    def entity_to_model(self, entity: domain.Exhibition) -> models.ExhibitionModel:
        return models.ExhibitionModel(
            exhibition_id=entity.exhibition_id,
            curator_id=entity.curator_id,
            exhibition_name=entity.exhibition_name,
            exhibition_description=entity.exhibition_description,
        )


@Translator.register_translator(models.ArtWorkModel)
class ArtWorkTranslator(Translator[models.ArtWorkModel, domain.ArtWork]):
    def model_to_entity(self, model: models.ArtWorkModel) -> domain.ArtWork:
        return domain.ArtWork(
            artwork_id=model.artwork_id,
            owner=model.owner,
            title=model.title,
            s3_key=model.s3_key,
            status=domain.ArtworkStatus(model.status),
            palette=domain.ArtWorkPalette(
                red=model.palette.red,
                green=model.palette.green,
                blue=model.palette.blue,
            ),
        )

    def entity_to_model(self, entity: domain.ArtWork) -> models.ArtWorkModel:
        return models.ArtWorkModel(
            artwork_id=entity.artwork_id,
            owner=entity.owner,
            title=entity.title,
            s3_key=entity.s3_key,
            status=entity.status.value,
            palette=models.ArtColorPaletteModel(
                red=entity.palette.red,
                green=entity.palette.green,
                blue=entity.palette.blue,
            ),
        )
