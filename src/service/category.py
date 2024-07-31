from database.config import supabase

class categoryService:
    def getCategoryList(self):
        response = supabase.table("Category").select("CategoryName", "Picture").order('CategoryName', desc=True).execute()
        return response.data