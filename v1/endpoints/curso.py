from typing import List 
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select 

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session
