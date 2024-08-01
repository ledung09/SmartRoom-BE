from database.supabase import supabase

class categoryService:
    def getCategoryList(self):
        response = supabase.table("Category").select("CategoryName", "Picture").order('CategoryName', desc=False).execute()
        return response.data