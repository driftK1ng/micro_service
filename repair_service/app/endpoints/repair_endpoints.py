from fastapi import APIRouter, HTTPException, Body, Depends, Header
from app.settings import settings
from app.service.repair_service import RepairService
from app.logger.logger_settings import LoggerSetup
from app.models.repair import Repair, RepairStatuses
from logging import getLogger
from uuid import uuid4
from datetime import datetime
from app.request.request_module import check_token
from uuid import UUID

repair_router = APIRouter(prefix='/repair', tags=['Repairs'])
logger_setup = LoggerSetup()
logger = getLogger(__name__)

@repair_router.get('/')
def get_repairs(repair_service: RepairService = Depends(RepairService)):
    return repair_service.get_repairs()

@repair_router.get('/{repair_id}')
def get_repair(repair_id: UUID, repair_service: RepairService = Depends(RepairService)):
    try:
        return repair_service.get_repair(repair_id)
    except KeyError:
        raise HTTPException(404, "router action: unknown repair id")

@repair_router.post('/create')
def create_repair(repair: Repair, token: str = Header(), repair_service: RepairService = Depends(RepairService)):
    validate_user(token)
    try:
        return repair_service.create_repair(repair)
    except KeyError:
        raise HTTPException(404, 'router action: id already exists')

@repair_router.post('/{repair_id}/activate')
def activate_repair(repair_id: UUID, token: str = Header(), repair_service: RepairService = Depends(RepairService)):
    validate_service(token)
    try:
        return repair_service.activate_repair(repair_id=repair_id)
    except KeyError:
        raise HTTPException(404, "router action: unknown repair id")
    except ValueError:
        raise HTTPException(400, "router action: bad repair status")

@repair_router.post('/{repair_id}/finish')
def finish_repair(repair_id: UUID, token: str = Header(), repair_service: RepairService = Depends(RepairService)):
    validate_service(token)
    try:
        return repair_service.finish_repair(repair_id=repair_id)
    except KeyError:
        raise HTTPException(404, "router action: unknown repair id")
    except ValueError:
        raise HTTPException(400, "router action: bad repair status")

@repair_router.post('/{repair_id}/delete')
def delete_repair(repair_id: UUID, token: str = Header(), repair_service: RepairService = Depends(RepairService)):
    validate_service(token)
    try:
        return repair_service.delete_repair(repair_id)
    except KeyError:
        raise HTTPException(404, "router action: unknown repair id")


def validate_service(token: str):
    if settings.test_build:
        return
    userdata = check_token(token)
    if userdata.status_code != 200:
        raise HTTPException(401, "bad token data")
    if 'service' not in userdata.json()['roles']:
        raise HTTPException(401, "Account dont have permissions")


def validate_user(token: str):
    if settings.test_build:
        return
    userdata = check_token(token)
    if userdata.status_code != 200:
        raise HTTPException(401, "bad token data")