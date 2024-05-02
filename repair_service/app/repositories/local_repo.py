from uuid import UUID
from app.models.repair import Repair
from app.logger.logger_settings import LoggerSetup


repairs: list[Repair] = []

class LocalRepo():
    def get_repairs(self):
        return repairs
    
    def get_repair(self, id: UUID):
        for repair in repairs:
            if repair.id == id:
                return repair
        return None
    
    def create_repair(self, repair: Repair):
        repairs.append(repair)
        return repair
    
    def change_repair(self, new_repair: Repair):
        for repair in repairs:
            if repair.id == new_repair.id:
                repairs.remove(repair)
                repairs.append(new_repair)
                return new_repair

    def delete_repair(self, new_repair: Repair):
        for repair in repairs:
            if repair.id == new_repair.id:
                repairs.remove(repair)
                return repair