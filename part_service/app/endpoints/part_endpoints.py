from fastapi import APIRouter, Depends, HTTPException, Body, Header
from app.service.part_service import PartService
from app.models.part import Part
from app.logger.logger_settings import LoggerSetup
from app.settings import settings
from app.auth_module.auth import check_token
from uuid import UUID
from logging import getLogger

part_router = APIRouter(prefix='/part', tags=['Parts'])
logger_setup = LoggerSetup()
logger = getLogger(__name__)


@part_router.get('/')
async def get_parts(part_service: PartService = Depends(PartService)):
    logger.info('router action: get_all_parts success)')
    
    return part_service.get_parts()


@part_router.get('/{part_id}')
async def get_parts(part_id: UUID, part_service: PartService = Depends(PartService)):
    try:
        logger.info('router action: get_part)')
        return part_service.get_part(part_id)
    except KeyError:
        raise HTTPException(404, "part with this id not found")
    
@part_router.post('/')
async def create_part(part: Part, token: str = Header(), part_service: PartService = Depends(PartService)):
    try:
        logger.info('router action: create_part')
        validate_user(token)
        return part_service.create_part(part)
    except KeyError:
        raise HTTPException(404, "part with this id already exists")
    except ValueError:
        raise HTTPException(401, "bad token")
    
@part_router.put('/')
async def change_part(part: Part, token: str = Header(), part_service: PartService = Depends(PartService)):
    try:
        logger.info('router action: change_part')
        validate_user(token)
        return part_service.change_part(part)
    except KeyError:
        raise HTTPException(404, "part with this id not found")
    except ValueError:
        raise HTTPException(401, "bad token")
    
@part_router.delete('/')
async def change_part(part: Part, token: str = Header(), part_service: PartService = Depends(PartService)):
    try:
        logger.info('router action: delete_part')
        validate_user(token)
        return part_service.delete_part(part)
    except KeyError:
        raise HTTPException(404, "part with this id not found")
    except ValueError:
        raise HTTPException(401, "bad token")


def validate_user(token: str):
    if settings.test_build:
        return
    userdata = check_token(token)
    if userdata.status_code != 200:
        raise ValueError