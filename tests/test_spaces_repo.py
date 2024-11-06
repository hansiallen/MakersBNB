from lib.spaces_repo import SpacesRepo
from mock import Mock

# This is an example of how to use the DatabaseConnection class
from lib.spaces_repo import *
"""
users should be able to find all spaces on the db
"""
def test_database_seed(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")

   # Retrieve all records
    result = db_connection.execute("SELECT * FROM spaces")

    # Assert that the results are what we expect
    assert result == [
              {
                  'description': 'A cozy cottage in the countryside',
                  'owner_id': 1,
                  'price_per_night': 100.00,
                  'space_id': 1,
                  'name': 'Cozy Cottage',
              },
              {
                  'description': 'A stylish loft in the city',
                  'owner_id': 2,
                  'price_per_night': 150.00,
                  'space_id': 2,
                  'name': 'Urban Loft',
              },
              {
                  'description': 'A relaxing beach house with ocean views',
                  'owner_id': 3,
                  'price_per_night': 200.00,
                  'space_id': 3,
                  'name': 'Beach House',
              },
          ]
    

def test_get_space(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    repo = SpacesRepo(db_connection)
   # Retrieve all records
    result = repo.get_space(2)

    # Assert that the results are what we expect
    assert result == [
              
              {
                  'description': 'A stylish loft in the city',
                  'owner_id': 2,
                  'price_per_night': 150.00,
                  'space_id': 2,
                  'name': 'Urban Loft',
              }
          ]
    


def test_add_space(db_connection):
    
    """Test adding a new space"""
    spaces_repo = SpacesRepo(db_connection)
    db_connection.execute('Delete FROM spaces')
    space = Mock()
    space.id = 5
    space.owner_id= 1
    space.price_per_night= 150.00
    space.space_id= 2,
    space.name= 'Urban Loft'
    space.description = ''
    spaces_repo.add_space(space)
    assert len(spaces_repo.list_spaces()) == 1
    assert spaces_repo.get_space(5).name == space.name

def test_remove_space(db_connection):
    """Test removing a new space"""
    db_connection.execute('Delete FROM spaces')
    spaces_repo = SpacesRepo(db_connection)
    space = Mock()
    space.id = 6
    space.owner_id= 1
    space.price_per_night= 150.00
    space.space_id= 2,
    space.name= 'Urban Loft'
    space.description = ''
    spaces_repo.add_space(space)
    spaces_repo.remove_space(6)
    assert len(spaces_repo.list_spaces()) == 0

def test_get_space(db_connection):
    """Test getting space"""
    spaces_repo = SpacesRepo(db_connection)
    space = Mock()
    space.id = 1
    space.owner_id= 1
    space.price_per_night= 150.00
    space.space_id= 2,
    space.name= 'Urban Loft'
    space.description = ''
    spaces_repo.add_space(space)
    retrieved_space = spaces_repo.get_space(1)
    assert retrieved_space.id == space.id

def test_get_multiple_spaces(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.execute('Delete FROM spaces')
    """Test getting space"""
    spaces_repo = SpacesRepo(db_connection)
    space1 = Mock()
    space1.id = 1
    space1.owner_id= 1
    space1.price_per_night= 150.00
    space1.space_id= 2,
    space1.name= 'Urban Loft 1'
    space1.description = ''
    spaces_repo.add_space(space1)
    space2 = Mock()
    space2.id = 2
    space2.owner_id= 1
    space2.price_per_night= 150.00
    space2.space_id= 2,
    space2.name= 'Urban Loft 2'
    space2.description = ''
    spaces_repo.add_space(space2)
    space3 = Mock()
    space3.id = 3
    space3.owner_id= 1
    space3.price_per_night= 150.00
    space3.space_id= 2,
    space3.name= 'Urban Loft 3'
    space3.description = ''
    spaces_repo.add_space(space3)
    retrieved_space = spaces_repo.get_space(5)
    assert retrieved_space.name == space2.name
    spaces_repo.remove_space(5)
    assert spaces_repo.get_space(5) == None