from bson import ObjectId
from fastapi import HTTPException
import json
import time
from typing import Optional, Union
from bson import ObjectId, json_util
from fastapi import FastAPI
from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pymongo import MongoClient
import os

import django


django.setup()
from django.contrib.auth import get_user_model
from user.models import UserProfile
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


User = get_user_model()
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "root")
MONGO_HOST = os.environ.get("MONGO_HOST", "mongo")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
# UserProfile = get_userprofile_model()

app = FastAPI()

client = MongoClient(
    f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
)

# MONGO_DETAILS = "mongodb://root:root@172.21.0.2:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client["project_data"]


class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type, handler
    ) -> core_schema.CoreSchema:
        """
        Defines the core schema for PyObjectId, which includes validation logic.
        """
        return core_schema.general_plain_validator_function(cls.validate)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema: JsonSchemaValue, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        """
        Updates the JSON schema for OpenAPI documentation.
        """
        schema.update(type="string", pattern="^[a-fA-F0-9]{24}$")
        return schema

    @classmethod
    def validate(cls, v):
        """
        Validation logic to ensure the value is a valid ObjectId.
        """
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


class Project(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        populate_by_name = True


@app.get("/")
def read_root():
    # return {"Hello": "World"}
    users = User.objects.values("username", "email", "id")
    return [
        {"username": i.get("username"), "email": i.get(
            "email"), "id": i.get("id")}
        for i in users
    ]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/profile")
def profile():
    users = UserProfile.objects.values("id")
    data = []
    for i in users:
        data.append({"id": i.id})
    return data


@app.get("/ping")
def ping():
    print("Hello")
    time.sleep(5)
    print("bye")
    return {"ping": "pong!"}


@app.get("/test-mongo")
def test_m():
    # m_d=database.project_col.insert_one({"name":"binod"})
    query_data = database.project_col.find()
    # json.dumps(list(m_d))
    # print(database.list_collection_names())
    data_json = json.loads(json_util.dumps(query_data))
    return data_json


