from uuid import UUID
from app.models.part import Part


class Repo():
    def get_parts(self):
        pass
    
    def get_part(self, id: UUID):
        pass
        
    def create_part(self, part):
        pass
    
    def change_part(self, new_part: Part):
        pass

    def delete_part(self, id):
        pass