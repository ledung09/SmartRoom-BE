from database.config import supabase

class categoryService:
    def getCategoryList(self):
        response = supabase.table("Category").select("*").execute()
        return response