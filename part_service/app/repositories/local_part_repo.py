from app.models.part import Part
from app.repositories.repo import Repo
from uuid import UUID, uuid4
parts: list[Part] = [
    Part(id=uuid4(), name='Деталь 1', description='Описание 1', price=100),
    Part(id=uuid4(), name='Деталь 2', description='Описание 2', price=200)
]

class PartRepo(Repo):

    def get_parts(self):
        return parts
    
    def get_part(self, id: UUID):
        for part in parts:
            if part.id == id:
                return part
        else:
            return None
        
    def create_part(self, part):
        parts.append(part)
        return part
    
    def change_part(self, new_part: Part):
        for part in parts:
            if part.id == new_part.id:
                parts.remove(part)
                parts.append(new_part)
                return new_part
        return None

    def delete_part(self, delete_part: Part):
        for part in parts:
            if part.id == delete_part.id:
                parts.remove(part)
                return part
        return None