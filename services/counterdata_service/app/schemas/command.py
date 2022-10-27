from pydantic import BaseModel, Field

class Scene(BaseModel):
    data: dict= Field(title='Конфигурация сцены')

class Command(BaseModel):
    scene: Scene = Field(title='Конфигурация сцены команды')