from fastapi import FastAPI, Body, HTTPException
from app.endpoints.part_endpoints import part_router
from prometheus_fastapi_instrumentator import Instrumentator
from logging import getLogger
from app.logger.logger_settings import LoggerSetup
from app.auth_module.auth import auth
from app.settings import settings

logger_settings = LoggerSetup()
logger = getLogger(__name__)

app = FastAPI(title="Part Service")

Instrumentator().instrument(app).expose(app)


@app.on_event('startup')
def on_startup():
    if settings.test_build:
        logger.warning('test build active')
        logger.warning('local repo active')
        logger.info('create container with flag (TEST_BUILD = False)')

@app.post('/auth')
def auth_user(username: str = Body(), password: str = Body()):
    logger.info('main router action: auth user')
    user = auth(username=username, password=password)
    print(user)
    if (user.status_code != 200):
        logger.warning('main router action: bad user data')
        raise HTTPException(401, 'bad user data')
    return user.json()['access_token']

app.include_router(part_router, prefix='/api')