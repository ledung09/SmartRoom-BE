from database.mongoDB import db

class esService:
    def getSearchResult(self, query: str):
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