from database.supabase import supabase

class categoryService:
    def getCategoryList(self):
        response = supabase.table("category").select("category_id", "category_name", "picture").order('category_name', desc=False).execute()
        return response.data