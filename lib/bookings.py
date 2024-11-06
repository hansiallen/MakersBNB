class Booking:
    def __init__(self, booking_id, space_id, user_id, booking_date):
        self.booking_id = booking_id
        self.space_id = space_id
        self.user_id = user_id
        self.booking_date = booking_date

    def __eq__(self, other):
        if not isinstance(other, Booking):
            return False
        return (self.booking_id == other.booking_id and
                self.space_id == other.space_id and
                self.user_id == other.user_id and
                self.booking_date == other.booking_date)
    
    def __repr__(self):
        return f"<Booking {self.booking_id} for Space {self.space_id} by User {self.user_id} on {self.booking_date}>"
