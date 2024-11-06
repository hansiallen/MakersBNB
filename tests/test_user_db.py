from lib.user_repo import *

def test_database_seed(db_connection):
    db_connection.seed("seeds/users.sql")

    result = db_connection.execute("SELECT * FROM users")

    assert result == [
              {
                  'email': 'user1@example.com',
                  'user_id': 1,
                  'name': "User One",
                  'password': 'password1',
              },
              {
                  'email': 'user2@example.com',
                  'user_id': 2,
                  'name': "User Two",
                  'password': 'password2',
              },
              {
                  'email': 'user3@example.com',
                  'user_id': 3,
                  'name': "User Three",
                  'password': 'password3',
              },
          ]