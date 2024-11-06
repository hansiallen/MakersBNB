from lib.spaces import Space
class SpacesRepo:
    def __init__(self,con):
        self.db_connection = con
        self.next_id = 1
    

    def add_space(self, space):
        self.db_connection.execute('INSERT INTO spaces (owner_id, name, description, price_per_night) values (%s, %s, %s, %s)',[space.owner_id,space.name, space.description, space.price_per_night])

    def remove_space(self, space_id):
        if self.db_connection.execute("DELETE FROM spaces WHERE space_id = %s",[space_id]):
          return True
        return False

    def get_space(self, space_id):
        item = self.db_connection.execute("SELECT * FROM spaces WHERE space_id = %s",[space_id])
        if item == []: return None
        item = item[0]
        result =  Space(item["space_id"], item["owner_id"], item["name"], item['description'], item['price_per_night'])
        return result
    
    def list_spaces(self):
        return list(self.db_connection.execute("SELECT * FROM spaces"))
