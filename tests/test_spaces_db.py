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
                  'title': 'Cozy Cottage',
              },
              {
                  'description': 'A stylish loft in the city',
                  'owner_id': 2,
                  'price_per_night': 150.00,
                  'space_id': 2,
                  'title': 'Urban Loft',
              },
              {
                  'description': 'A relaxing beach house with ocean views',
                  'owner_id': 3,
                  'price_per_night': 200.00,
                  'space_id': 3,
                  'title': 'Beach House',
              },
          ]
    

def test_database_seed(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    repo = SpacesRepo()
   # Retrieve all records
    result = repo.get_space(2)

    # Assert that the results are what we expect
    assert result == [
              
              {
                  'description': 'A stylish loft in the city',
                  'owner_id': 2,
                  'price_per_night': 150.00,
                  'space_id': 2,
                  'title': 'Urban Loft',
              }
          ]
    
