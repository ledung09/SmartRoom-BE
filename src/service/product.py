import asyncio
from database.mongoDB import db
from database.supabase import supabase
from fastapi import HTTPException

class productService:    
    async def getProductDetail(self, id: str):
        product = db['core']['products'].find_one({ "_id" : id })

        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")

        return product
    

    async def getProductSupplierDetail(self, id: str):
        response = supabase.table("product_supplier_fulldetail").select(
            'supplier_id',
            'supplier_name',
            'supplier_type_goods',
            'supplier_image',
            'supplier_product_count',
            'supplier_rating').eq("product_id", id).execute()
        
        if len(response.data) == 0:
            raise HTTPException(status_code=500, detail="Product not found")
    
        return response.data[0]
    
    async def getProductFullDetail(self, id: str):
        mongo_data, supabase_data = await asyncio.gather(self.getProductDetail(id), self.getProductSupplierDetail(id))
        return {**mongo_data, **supabase_data}