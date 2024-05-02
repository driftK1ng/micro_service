from app.repositories.local_part_repo import PartRepo
from app.models.part import Part
from app.logger.logger_settings import LoggerSetup
from app.settings import settings
from logging import getLogger
from uuid import UUID

logger_setup = LoggerSetup()
logger = getLogger(__name__)


class PartService():
    def __init__(self) -> None:
        self.part_repo = PartRepo()

    def get_parts(self) -> list[Part]:
        logger.info('backend action: get all part success')
        return self.part_repo.get_parts()

    def get_part(self, id: UUID) -> Part:
        logger.info('backend action: get part by id success')
        data = self.part_repo.get_part(id=id)
        if data == [] or data is None:
            logger.warning('backend action: get part by id (unknown id) error')
            raise KeyError
        logger.info('action: get part by id success')
        return self.part_repo.get_part(id=id)

    def create_part(self, part: Part) -> Part:
        if self.part_repo.get_part(part.id) is not None:
            logger.warning('backend action: create part (same id) error')
            raise KeyError
        logger.info(f'create new part {part.name} success')
        return self.part_repo.create_part(part=part)

    def change_part(self, part: Part) -> Part:
        if self.part_repo.get_part(part.id) is None:
            logger.warning('backend action: changing part (unknown id) error')
            raise KeyError
        logger.info(f'backend action: change part {part.name} success')
        return self.part_repo.change_part(new_part=part)

    def delete_part(self, part: Part) -> Part:
        if self.part_repo.get_part(part.id) is None:
            logger.warning('backend action: deleting part (unknown id) error')
            raise KeyError
        logger.info(f'backend action: delete part {part.name} success')
        return self.part_repo.delete_part(part)
