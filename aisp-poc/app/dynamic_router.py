from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Any
from app.db import client as sb_client
from app.agent import GenericAgent

router = APIRouter()

def build():
    rows = sb_client().table("components").select("*").eq("status", "ready").execute().data
    for row in rows:
        cid = row["id"]
        aisp = row["json_spec"]["AISP"] if "AISP" in row["json_spec"] else row["aisp"]
        payload_model = type(f"{cid}Model", (BaseModel,), {
            "id":   (int | None, Field(default=None)),
            "name": (str, Field(...))
        })

        async def handler(body: payload_model, _aisp=aisp):
            agent = GenericAgent(_aisp)
            return await agent.invoke(body.dict())

        router.post(f"/{cid}", name=f"{cid}_create")(handler)

build()