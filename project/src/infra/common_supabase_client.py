import os
from supabase import create_client, Client


class CommonSupabaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommonSupabaseClient, cls).__new__(cls)
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_ANON_KEY")
            cls._instance.client = create_client(url, key)
        return cls._instance

    def client(self) -> Client:
        return self._instance.client
