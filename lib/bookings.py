from datetime import datetime

class Booking:
    def __init__(self, id, user_id, space_id, start_date, end_date, status="pending"):
        self.id = id
        self.user_id = user_id
        self.space_id = space_id
        self.start_date = datetime.strptime(start_date, "%d-%m-%Y")
        self.end_date = datetime.strptime(end_date, "%d-%m-%Y")
        self.status = status  # Can be "pending", "confirmed", or "canceled"

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.user_id == other.user_id and
            self.space_id == other.space_id and
            self.start_date == other.start_date and
            self.end_date == other.end_date and
            self.status == other.status
        )
    
    #Used str for better user readability
    def __str__(self):
        # User-readable summary of the booking
        return f"Booking {self.id}: User {self.user_id} for Space {self.space_id} from {self.start_date.strftime('%d-%m-%Y')} to {self.end_date.strftime('%d-%m-%Y')}, Status: {self.status}"
    
    def __repr__(self):
        return f"Booking(id={self.id}, user_id={self.user_id}, space_id={self.space_id}, start_date={self.start_date.strftime('%d-%m-%Y')}, end_date={self.end_date.strftime('%d-%m-%Y')}, status='{self.status}')"
