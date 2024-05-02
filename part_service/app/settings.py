from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    test_build: bool
    keycloak_url: str
    keycloak_realm: str
    keycloak_secret: str
    keycloak_id: str
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()