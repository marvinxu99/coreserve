# define a class that will act as an interface to your data 
# storage layer (e.g., SQL database, NoSQL, or in-memory data).

class FHIRService:
    def __init__(self):
        self.db = {}            # A placeholder for actual database

    def save_resource(self, resource):
        self.db[resource.id] = resource

    def get_resource(self, resource_type, resource_id):
        return self.db.get(resource_id)

    def update_resource(self, resource_type, resource_id, resource):
        if resource_id in self.db:
            self.db[resource_id] = resource
            return resource
        return None

    def delete_resource(self, resource_type, resource_id):
        return self.db.pop(resource_id, None)
