from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class CursoSchema(SchemaBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    instrutor: str

    class Config:
        orm_mode=True