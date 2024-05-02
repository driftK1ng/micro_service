from fastapi import FastAPI, Body, HTTPException
from app.endpoints.repair_endpoints import repair_router
from prometheus_fastapi_instrumentator import Instrumentator
from logging import getLogger
from app.logger.logger_settings import LoggerSetup
from app.request.request_module import auth
import asyncio
from app.rabbitmq import rabbit
from app.settings import settings

logger_settings = LoggerSetup()
logger = getLogger(__name__)

app = FastAPI(title="Repair Service")

Instrumentator().instrument(app).expose(app)


@app.on_event('startup')
def on_startup():
    if not settings.test_build:
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(rabbit.consume(loop))

@app.post('/auth')
def auth_user(username: str = Body(), password: str = Body()):
    logger.info('main router action: auth user')
    user = auth(username=username, password=password)
    print(user)
    if (user.status_code != 200):
        logger.warning('main router action: bad user data')
        raise HTTPException(401, 'bad user data')
    return user.json()['access_token']

app.include_router(repair_router, prefix='/api')