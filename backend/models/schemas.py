from pydantic import BaseModel
from typing import List, Dict, Any


class Intent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]


class Architecture(BaseModel):
    entities: List[str]
    pages: List[str]
    roles: List[str]


class UISchema(BaseModel):
    pages: List[Dict[str, Any]]


class APISchema(BaseModel):
    endpoints: List[Dict[str, Any]]


class DBSchema(BaseModel):
    tables: List[Dict[str, Any]]


class AuthSchema(BaseModel):
    roles: Dict[str, List[str]]


class AppConfig(BaseModel):
    ui: UISchema
    api: APISchema
    database: DBSchema
    auth: AuthSchema