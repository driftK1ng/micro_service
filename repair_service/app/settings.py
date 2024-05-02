from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    amqp_url: str
    test_build: bool
    postgres_url: str
    keycloak_url: str
    keycloak_realm: str
    keycloak_secret: str
    keycloak_id: str
    parts_url: str
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()