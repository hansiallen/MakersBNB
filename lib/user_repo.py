from lib.user import User

class UserRepo:
    def __init__(self, db_connection):
        self.db_connection = db_connection  # Expecting a database connection object

    def add_user(self, user):
        """Add a user to the database."""
        # Insert email and password only, ignoring the name field
        query = "INSERT INTO users (email, password) VALUES (%s, %s) RETURNING user_id"
        result = self.db_connection.execute(query, (user.email, user.password, ))
    
        if result:
            return result[0]['user_id']
        else:
            raise ValueError("Failed to add user to the database.")
        
    def remove_user(self, user_id):
        """Remove a user from the database by ID."""
        query = "DELETE FROM users WHERE user_id = %s"
        result = self.db_connection.execute(query, (user_id,))
        if result is not None and len(result) > 0:  # Check if result is not None and affected
            return True
        return False

    def get_user(self, user_id):
        """Get a user from the database by ID."""
        query = "SELECT user_id, email, password FROM users WHERE user_id = %s"
        result = self.db_connection.execute(query, (user_id,))
        if result:
            user_data = result[0]
            return User(user_data['user_id'], user_data['email'], user_data['password'])  # Remove user_data['name']
        return None
    
    def get_user_by_id(self, user_id):
        """Get a user from the database by ID."""
        query = "SELECT user_id, email, password FROM users WHERE user_id = %s"
        result = self.db_connection.execute(query, (user_id,))
        if result:
            user_data = result[0]
            return User(user_data['user_id'], user_data['email'], user_data['password'])  # Remove user_data['name']
        return None
    
    def get_user_by_email(self, email):
        """Get a user from the database by email."""
        query = "SELECT user_id, email, password FROM users WHERE email = %s"
        result = self.db_connection.execute(query, (email,))
        if result:
            user_data = result[0]
            return User(user_data['user_id'], user_data['email'], user_data['password'])  # Return User object
        return None

    def list_users(self):
        """Retrieve a list of users from the database."""
        query = "SELECT user_id, email, password FROM users"
        result = self.db_connection.execute(query)
        
        # Now we expect to return a list of users with only email and password (no name)
        return [User(row['user_id'], row['email'], row['password']) for row in result]