# lib/booking_repo.py

from lib.database_connection import DatabaseConnection
from lib.bookings import Booking

class BookingRepo:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def add_booking(self, booking: Booking):
        query = """
        INSERT INTO bookings (space_id, user_id, booking_date)
        VALUES (%s, %s, %s)
        RETURNING booking_id;
        """
        result = self.db_connection.execute(query, [booking.space_id, booking.user_id, booking.booking_date])
        booking.booking_id = result[0]['booking_id']
        return booking

    def get_booking(self, booking_id: int):
        query = "SELECT * FROM bookings WHERE booking_id = %s;"
        result = self.db_connection.execute(query, [booking_id])
        if result:
            return Booking(result[0]['booking_id'], result[0]['space_id'], result[0]['user_id'], result[0]['booking_date'])
        return None
    
    def list_bookings(self):
        query = "SELECT * FROM bookings;"
        results = self.db_connection.execute(query)
        return [Booking(row['booking_id'], row['space_id'], row['user_id'], row['booking_date']) for row in results]
    
    def remove_booking(self, booking_id: int):
        query = "DELETE FROM bookings WHERE booking_id = %s;"
        result = self.db_connection.execute(query, [booking_id])
        return result > 0
