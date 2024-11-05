class Booking:
    def __init__(self, booking_id, space_id, user_id, booking_date):
        self.booking_id = booking_id
        self.space_id = space_id
        self.user_id = user_id
        self.booking_date = booking_date

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "space_id": self.space_id,
            "user_id": self.user_id,
            "booking_date": self.booking_date,
        }

    def __repr__(self):
        return f"<Booking {self.booking_id} for space {self.space_id} by user {self.user_id} on {self.booking_date}>"
