from os import getenv
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = getenv("SUPABASE_URL")
key: str = getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)