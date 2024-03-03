import datetime
from sqlmodel import SQLModel, Field, create_engine
from config import config

class PredictionResult(SQLModel, table=True):
    id: int=Field(default=None, primary_key=True)
    result: int
    created_at: str = Field(default_factory=datetime.datetime.now)
    #default_factory: deafault값을 동적으로 지정

engine = create_engine(config.db_url)