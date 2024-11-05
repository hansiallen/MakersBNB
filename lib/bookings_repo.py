from lib.bookings import Booking

class BookingsRepo:
    def __init__(self):
        self.bookings = {} 

    def create_booking(self, id, user_id, space_id, start_date, end_date, status="pending"):
        if id in self.bookings:
            raise ValueError("Booking ID already exists")
        
        new_booking = Booking(id, user_id, space_id, start_date, end_date, status)
        self.bookings[id] = new_booking
        return new_booking

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)

    def get_bookings_by_space(self, space_id):
        return [booking for booking in self.bookings.values() if booking.space_id == space_id]

    def update_booking_status(self, booking_id, new_status):
        if booking_id not in self.bookings:
            raise ValueError("Booking not found")
        
        self.bookings[booking_id].status = new_status
        return self.bookings[booking_id]

    def remove_booking(self, booking_id):
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False
