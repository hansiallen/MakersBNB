from lib.user_repo import *

def test_database_seed(db_connection):
    db_connection.seed("seeds/users.sql")

    result = db_connection.execute("SELECT * FROM users")

    assert result == [
              {
                  'email': 'user1@example.com',
                  'user_id': 1,
                  'password': 'scrypt:32768:8:1$S3VeFkMUqtf7mwHw$68cf3b8e7f2897b3e3e6ecc4ad225f105ed4ca19cba629bd5cb5d9b59e8dec1986cc8f3fa3bdc566946b94fbc83d92afc2ca05d00a90238fa03271423d8199ef',
              },
              {
                  'email': 'user2@example.com',
                  'user_id': 2,
                  'password': 'scrypt:32768:8:1$xR9ixcSIknXCfJO5$d7f56eec54e5619b0b858cc99d00320259da54f12632945415548ddb88a14001409874899f54603705750783ced8be5ceaeebd9fb8315ef45c32c47f802672cf',
              },
              {
                  'email': 'user3@example.com',
                  'user_id': 3,
                  'password': 'scrypt:32768:8:1$XRymBxBDtZw1JxXM$a3e61b2377ffd872d8faa4d4308dec7c2ae28a12299d67019e02015e733a3ffd9f82d4bec7d51bc2e4d755cb80bb0e764cb672017e54d631a76ca511a735f100',
              },
          ]