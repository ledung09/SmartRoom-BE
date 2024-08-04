from database.mongoDB import db

class esService:
    def getSearchResult(
        self, 
        query: str, 
        categoryId: int, 
        priceSort: int, 
        soldSort: int,
        limit: int,
        offset: int
    ):
        print(limit)

        # Initialize pipeline
        pipeline = []

        # Add $search stage if query is not empty
        if query:
            pipeline.append({
                "$search": {
                    "index": "searchProducts",
                    "text": {
                        "query": query,
                        "path": ["name", "description"],
                        "fuzzy": {}
                    }
                }
            })

            if categoryId is not None:
                pipeline.append({
                    "$match": {
                        "category_id": categoryId
                    }
                })

            pipeline.append({
                "$addFields": {
                    "score": { "$meta": "searchScore" }
                }
            })
        else:
            if categoryId is not None:
                pipeline.append({
                    "$match": {
                        "category_id": categoryId
                    }
                })

        # Handle sort selection
        sort_stage = {}
        if priceSort is not None:
            sort_stage["price"] = priceSort
        if soldSort is not None:
            sort_stage["sold"] = soldSort

        # Ensure the results are sorted by score if no other sort is provided
        if not sort_stage and query:
            sort_stage = { "score": -1 }

        if sort_stage:
            pipeline.append({
                "$sort": sort_stage
            })

        # Add the remaining stages
        pipeline.extend([
            {
                "$project": {
                    "name": 1,
                    "image": 1,
                    "price": 1,
                    "sold": 1,
                }
            },
            {
                "$skip": offset
            },
            {
                "$limit": limit
            }
        ])

        # Execute the aggregation pipeline
        mongo_res = db["core"]["products"].aggregate(pipeline)

        # Result cleaning
        response = []
        for res in list(mongo_res):
            response.append(res)

        return response


    
    def getAutoCompleteSearchResult(self, query: str):
        response = []
        mongo_res = db["core"]["products"].aggregate([
            { 
                "$search": { 
                    "index": "autoCompleteProducts", 
                    "autocomplete": { 
                        "query": query, 
                        "path": "name", 
                        "tokenOrder": "sequential",
                        "fuzzy": {
                            "maxEdits": 1
                        }
                    } 
                } 
            }, 
            { "$limit": 10 }, 
            { "$project": { 
                "name": 1,
                "_id": 0
                } 
            } 
        ])

        # result cleaning
        for res in list(mongo_res): 
            response.append(res['name'])

        return response