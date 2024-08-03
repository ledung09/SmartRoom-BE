from database.mongoDB import db

class esService:
    def getSearchResult(
        self, 
        query: str, 
        categoryId: int, 
        priceSort: int, 
        soldSort: int
    ):

        # initialize pipeline
        pipeline = []

        # come with search action first
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
            # Insert $match stage after $search
            pipeline.append({
                "$match": {
                    "category_id": categoryId
                }
            })

        # Add $addFields stage
        pipeline.append({
            "$addFields": {
                "score": { "$meta": "searchScore" }
            }
        })


        # handle sort selection
        sort_stage = {}
        if priceSort is not None:
            sort_stage["price"] = priceSort
        if soldSort is not None:
            sort_stage["sold"] = soldSort

        pipeline.append({
            "$sort": sort_stage if sort_stage else { "score": -1 }
        })


        # pipeline.append({
        #     "$sort": {
        #           # Sorting by score in descending order
        #     }
        # })

        # add the remaining stages
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
                "$skip": 0
            },
            {
                "$limit": 10
            }
        ])

        print(pipeline)


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