from lib.bookings import Booking

class BookingRepo:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_booking(self, booking):
        query = """
            INSERT INTO bookings (space_id, user_id, booking_date) 
            VALUES (%s, %s, %s) RETURNING booking_id
        """
        result = self.db_connection.execute(query, (booking.space_id, booking.user_id, booking.booking_date))
        if result:
            return result[0]['booking_id']
        else:
            raise ValueError("Failed to add booking to the database.")
        
    def remove_booking(self, booking_id):
        query = "DELETE FROM bookings WHERE booking_id = %s"
        self.db_connection._check_connection()
        with self.db_connection.connection.cursor() as cursor:
            cursor.execute(query, (booking_id,))
            self.db_connection.connection.commit()
            return cursor.rowcount > 0

    def get_booking(self, booking_id):
        query = "SELECT * FROM bookings WHERE booking_id = %s"
        result = self.db_connection.execute(query, (booking_id,))
        if result:
            booking_data = result[0]
            return Booking(
                booking_data['booking_id'],
                booking_data['space_id'],
                booking_data['user_id'],
                booking_data['booking_date']
            )
        return None

    def list_bookings(self):
        query = "SELECT * FROM bookings"
        results = self.db_connection.execute(query)
        return [Booking(row['booking_id'], row['space_id'], row['user_id'], row['booking_date']) for row in results]
