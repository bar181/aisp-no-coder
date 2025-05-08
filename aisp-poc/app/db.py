from functools import lru_cache
import os
from dotenv import load_dotenv
from supabase_py import create_client

load_dotenv()

@lru_cache
def client():
    return create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))