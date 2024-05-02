from uuid import UUID
import traceback
from app.models.repair import Repair
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.repair import Repair, RepairStatuses
from app.schemas.repair import Repair as DBRepair


class BdRepo():
    db: Session
    def __init__(self):
        self.db = next(get_db())

    def _map_to_model(self, repair: DBRepair) -> Repair:
        result = Repair.from_orm(repair)
        return result
    
    def _map_to_schema(self, repair: Repair) -> DBRepair:
        data = dict(repair)
        result = DBRepair(**data)
        return result

    def get_repairs(self):
        repairs = []
        for repair in self.db.query(DBRepair).all():
            temp = Repair.from_orm(repair)
            repairs.append(temp)
        return repairs
    
    def get_repair(self, id: UUID):
        repair = self.db.query(DBRepair).filter(DBRepair.id == id).first()
        return repair
    
    def create_repair(self, repair: Repair):
        try:
            db_repair = self._map_to_schema(repair)
            self.db.add(db_repair)
            self.db.commit()
            return repair
        except:
            traceback.print_exc()
            raise KeyError
    
    def change_repair(self, new_repair: Repair):
        db_order: DBRepair = self.db.query(DBRepair).filter(
            DBRepair.id == new_repair.id).first()
        db_order.description = new_repair.description
        db_order.part = new_repair.part
        db_order.repair_status = new_repair.repair_status
        self.db.commit()
        return self._map_to_model(db_order)

    def delete_repair(self, new_repair: Repair):
        db_repair = self.get_repair(new_repair.id)
        self.db.delete(db_repair)
        self.db.commit()
        return new_repair