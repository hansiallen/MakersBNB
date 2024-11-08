class Booking:
    def __init__(self, booking_id, space_id, user_id, start_date, end_date, accepted):
        if not start_date or not end_date:
            raise ValueError("Both start date and end date are required")
        self.booking_id = booking_id
        self.space_id = space_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.accepted = accepted
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"Booking({self.booking_id}, {self.space_id}, {self.user_id}, {self.start_date}, {self.end_date})"