import asyncio
from database.mongoDB import db
from database.supabase import supabase
from fastapi import HTTPException
from interface.product import HeartedProductUpdate

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
            raise HTTPException(status_code=404, detail="Product not found")
    
        return response.data[0]
    
    async def getProductHeartedDetail(self, id: str, userId: str):
        response = supabase.table("user_product").select('hearted').eq("product_id", id).eq("user_id", userId).execute()
        
        if len(response.data) == 0:
           return { "hearted": False }
    
        return response.data[0]
    
    async def getProductFullDetail(self, id: str, userId: str):
        productDetail, supplierDetail, heartedDetail = await asyncio.gather(
            self.getProductDetail(id), 
            self.getProductSupplierDetail(id),
            self.getProductHeartedDetail(id, userId))
        return {**productDetail, **supplierDetail, **heartedDetail}
    
    def setProductHeartedDetail(self, id: str, userId: str, updateHearted: HeartedProductUpdate):
        response = supabase.table("user_product").select('hearted').eq("product_id", id).eq("user_id", userId).execute()
        
        if len(response.data) == 0:
           return supabase.table("user_product").insert({"user_id": userId, "product_id": id, "hearted": True}).execute()

        return supabase.table("user_product").update({"hearted": updateHearted.hearted}).eq("product_id", id).eq("user_id", userId).execute()