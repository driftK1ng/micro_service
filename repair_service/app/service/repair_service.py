
from app.repositories.local_repo import LocalRepo
from app.models.repair import Repair, RepairStatuses
from app.settings import settings
from app.logger.logger_settings import LoggerSetup
from logging import getLogger
from uuid import UUID
import random
from app.request.request_module import get_parts, get_part
if not settings.test_build:
    from app.repositories.bd_repo import BdRepo

logger_settings = LoggerSetup()
logger = getLogger(__name__)

class RepairService():
    def __init__(self):
        if settings.test_build:
            self.repair_repo = LocalRepo()
        else:
            self.repair_repo = BdRepo()

    def create_repair(self, repair: Repair) -> Repair:
        logger.info('backend action: try to create new repair')
        if self.repair_repo.get_repair(repair.id) != None:
            logger.warning('backend action: error to create new repair (this id already exists)')
            raise KeyError
        repair.repair_status = RepairStatuses.CREATED
        logger.info('backend action: create new repair')
        return self.repair_repo.create_repair(repair)
    
    def activate_repair(self, repair_id: UUID) -> Repair:
        logger.info('backend action: try to activate repair')
        repair = self.repair_repo.get_repair(repair_id)
        if repair == None:
            logger.warning('backend action: error to activate repair (unknown id)')
            raise KeyError
        if repair.repair_status != RepairStatuses.CREATED:
            logger.warning('backend action: error to activate repair (bad status)')
            raise ValueError
        if not settings.test_build:
            part = random.choice(get_parts())
        if part != '':
            repair.part = part['id']
        repair.repair_status = RepairStatuses.PROCCESS
        logger.info('backend action: activate repair')
        return self.repair_repo.change_repair(repair)
    
    def finish_repair(self, repair_id: UUID) -> Repair:
        logger.info('backend action: try to finish repair')
        repair = self.repair_repo.get_repair(repair_id)
        if repair == None:
            logger.warning('backend action: error to finish repair (unknown id)')
            raise KeyError
        if repair.repair_status != RepairStatuses.PROCCESS:
            logger.warning('backend action: error to finish repair (bad status)')
            raise ValueError
        repair.repair_status = RepairStatuses.DONE
        logger.info('backend action: finish repair')
        return self.repair_repo.change_repair(repair)
    
    def delete_repair(self, repair_id: UUID) -> Repair:
        logger.info('backend action: try to delete repair')
        repair = self.repair_repo.get_repair(repair_id)
        if repair == None:
            logger.warning('backend action: error to delete repair (unknown id)')
            raise KeyError
        logger.info('backend action: delete repair')
        return self.repair_repo.delete_repair(repair)
    
    def get_repair(self, repair_id: UUID) -> Repair:
        logger.info('backend action: try to get repair')
        if self.repair_repo.get_repair(repair_id) == None:
            logger.warning('backend action: error to get repair (unknown id)')
            raise KeyError
        logger.info('backend action: get repair')
        data = self.repair_repo.get_repair(repair_id)
        data.part = get_part(data.part)
        return data
    
    def get_repairs(self) -> list[Repair]:
        logger.info('backend action: try to get all repair')
        return self.repair_repo.get_repairs()
    