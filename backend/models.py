from app import mongo

class Employee:
    @staticmethod
    def to_json(employee):
        return {
            "_id": str(employee["_id"]),
            "name": employee["name"],
            "role": employee["role"],
            "description": employee["description"],
            "gender": employee["gender"],
            "imgUrl": employee.get("imgUrl")
        }
