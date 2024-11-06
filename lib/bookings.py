class Booking:
    def __init__(self, booking_id, space_id, user_id, booking_date):
        if not booking_date:
            raise ValueError("Booking date is required")
        self.booking_id = booking_id
        self.space_id = space_id
        self.user_id = user_id
        self.booking_date = booking_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.booking_id}, {self.space_id}, {self.user_id}, {self.booking_date})"
