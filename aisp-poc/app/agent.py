"""
GenericAgent – minimal LLM wrapper that executes AISP instructions.
For Sprint 1 we simply echo the payload; real logic arrives in later sprints.
"""
import os, json
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_client = OpenAI()

class GenericAgent:
    def __init__(self, aisp: str):
        self.system_prompt = f"You are an API stub obeying this AISP:\n{aisp}"

    async def invoke(self, payload: dict):
        # For PoC return payload with echo
        return {"echo": payload}